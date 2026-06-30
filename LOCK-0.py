import os
import hashlib
import secrets
import customtkinter as ctk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import traceback
import sys
from PIL import Image, ImageTk
import struct
import time
from pathlib import Path

MAGIC_HEADER = b"BASIRAENC2"
VERSION = 2


def derive_key(password: str, salt: bytes):
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  
        salt=salt,
        iterations=600000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


def file_hash(data):
    return hashlib.sha256(data).hexdigest()


def safe_delete_file(path, log=None):
    try:
        file_size = os.path.getsize(path)
        
        with open(path, "ba+") as f:
            for _ in range(3):
                f.seek(0)
                f.write(os.urandom(file_size))
                f.flush()
                os.fsync(f.fileno())
        
        os.remove(path)
        if log:
            log(f"[X] The file was safely deleted: {os.path.basename(path)}")
        return True
        
    except Exception as e:
        if log:
            log(f"[!] Safe deletion error: {str(e)}")
        try:
            os.remove(path)
            return True
        except:
            return False


def encrypt_file(path, password, log):
    try:
        with open(path, "rb") as f:
            data = f.read()
        
        original_size = len(data)
        log(f"[ℹ] File processing: {os.path.basename(path)} (Size: {original_size} bytes)")

        original_hash = file_hash(data)
        
        salt = secrets.token_bytes(16)
        nonce = secrets.token_bytes(12)
        key = derive_key(password, salt)
        aes = AESGCM(key)
        encrypted = aes.encrypt(nonce, data, None)
        
        enc_path = path + ".enc"

        with open(enc_path, "wb") as f:
            f.write(MAGIC_HEADER)                           
            f.write(struct.pack('>I', VERSION))           
            f.write(struct.pack('>Q', original_size))     
            f.write(salt)                                   
            f.write(nonce)                                 
            f.write(encrypted)                              

        log(f"[✔] An encrypted file was created: {os.path.basename(enc_path)} (Size: {os.path.getsize(enc_path)} bytes)")

        with open(enc_path, "rb") as f:
            filedata = f.read()

        if len(filedata) < len(MAGIC_HEADER):
            log(f"[!] The encrypted file is very small.")
            safe_delete_file(enc_path, log)
            return False
            
        header = filedata[:len(MAGIC_HEADER)]
        if header != MAGIC_HEADER:
            log(f"[!] Incorrect Magic Header.")
            safe_delete_file(enc_path, log)
            return False

        offset = len(MAGIC_HEADER)
        
        if len(filedata) < offset + 4 + 8:
            log(f"[!] The file is missing version or size information.")
            safe_delete_file(enc_path, log)
            return False
        
        version = struct.unpack('>I', filedata[offset:offset+4])[0]
        offset += 4
        
        stored_size = struct.unpack('>Q', filedata[offset:offset+8])[0]
        offset += 8
        
        if version != VERSION:
            log(f"[!] The file version does not match.")
            safe_delete_file(enc_path, log)
            return False

        if len(filedata) < offset + 16 + 12:
            log(f"[!] The file is missing Salt or Nonce")
            safe_delete_file(enc_path, log)
            return False
            
        salt2 = filedata[offset:offset+16]
        offset += 16
        nonce2 = filedata[offset:offset+12]
        offset += 12
        encrypted2 = filedata[offset:]
        
        key2 = derive_key(password, salt2)
        aes2 = AESGCM(key2)
        
        try:
            decrypted = aes2.decrypt(nonce2, encrypted2, None)
        except Exception as e:
            log(f"[!] Decryption failed: {str(e)}")
            safe_delete_file(enc_path, log)
            return False

        if len(decrypted) != stored_size:
            log(f"[!] Size mismatch! Expected: {stored_size}, actual: {len(decrypted)}")
            safe_delete_file(enc_path, log)
            return False

        decrypted_hash = file_hash(decrypted)
        
        if decrypted_hash == original_hash:
            safe_delete_file(path, log)
            log(f"[✔] Successful encryption with secure deletion: {os.path.basename(path)}")
            return True
        else:
            log(f"[!] inconsistency Hash!")
            log(f"    Original: {original_hash[:16]}...")
            log(f"    Decrypted: {decrypted_hash[:16]}...")
            safe_delete_file(enc_path, log)
            return False

    except Exception as e:
        log(f"[!] Encryption error: {str(e)}")
        log(traceback.format_exc())
        if 'enc_path' in locals() and os.path.exists(enc_path):
            safe_delete_file(enc_path, log)
        return False


def decrypt_file(path, password, log):
    try:
        if not path.endswith('.enc'):
            log(f"[!] Unencrypted file: {os.path.basename(path)}")
            return False

        log(f"[ℹ] Attempting to decode: {os.path.basename(path)}")
        
        with open(path, "rb") as f:
            filedata = f.read()

        if len(filedata) < len(MAGIC_HEADER):
            log(f"[!] The file is very small.")
            return False

        header = filedata[:len(MAGIC_HEADER)]
        if header != MAGIC_HEADER:
            log(f"[!] Invalid file (Header wrong).")
            return False

        offset = len(MAGIC_HEADER)
        
        if len(filedata) < offset + 4 + 8:
            log(f"[!] The file is corrupted or incomplete.")
            return False
        
        version = struct.unpack('>I', filedata[offset:offset+4])[0]
        offset += 4
        
        stored_size = struct.unpack('>Q', filedata[offset:offset+8])[0]
        offset += 8

        if len(filedata) < offset + 16 + 12:
            log(f"[!] The file is corrupted or incomplete (Salt/Nonce).")
            return False
            
        salt = filedata[offset:offset+16]
        offset += 16
        nonce = filedata[offset:offset+12]
        offset += 12
        encrypted = filedata[offset:]

        key = derive_key(password, salt)
        aes = AESGCM(key)
        
        try:
            decrypted = aes.decrypt(nonce, encrypted, None)
        except Exception as e:
            log(f"[!] Decryption failed - Incorrect password?")
            log(f"    Error: {str(e)}")
            return False

        if len(decrypted) != stored_size:
            log(f"[!] Size mismatch! Expected: {stored_size}, actual: {len(decrypted)}")
            return False

        out_path = path.replace(".enc", "")
        
        counter = 1
        original_out_path = out_path
        while os.path.exists(out_path):
            name, ext = os.path.splitext(original_out_path)
            out_path = f"{name}_decrypted{counter}{ext}"
            counter += 1
        
        with open(out_path, "wb") as f:
            f.write(decrypted)
        
        log(f"[✔] Successful decryption: {os.path.basename(out_path)}")
        
        safe_delete_file(path, log)
        
        return True

    except Exception as e:
        log(f"[!] Decryption error:{str(e)}")
        return False


def process_folder(folder, password, mode, log):
    files_processed = 0
    files_failed = 0
    
    log(f"[ℹ] Starting the process{mode} in: {folder}")
    log(f"[ℹ] Password length: {len(password)}")
    log(f"[ℹ] Encryption version: v{VERSION} (PBKDF2 600K iterations)")
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            
            try:
                if mode == "encrypt":
                    if file.endswith('.enc'):
                        log(f"[>>] Previously encrypted file: {file}")
                        continue
                    
                    if file.startswith('.') or file.startswith('~'):
                        continue
                    
                    if encrypt_file(full_path, password, log):
                        files_processed += 1
                    else:
                        files_failed += 1
                        
                elif mode == "decrypt":
                    if file.endswith('.enc'):
                        if decrypt_file(full_path, password, log):
                            files_processed += 1
                        else:
                            files_failed += 1
                    else:
                        log(f"[>>] Unencrypted file: {file}")
                        
            except Exception as e:
                log(f"[!] Error in processing {file}: {str(e)}")
                files_failed += 1
    
    return files_processed, files_failed

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue") 

app = ctk.CTk()
app.title("LOCK-0 v1.0.0 - ENCRYPTION TOOL (SECURE)")
app.geometry("800x700")
app.resizable(False, False)

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

icon_ico = os.path.join(base_path, "L0.ico")
icon_png = os.path.join(base_path, "L0.png")  

if os.path.exists(icon_png):
    try:
        icon = ImageTk.PhotoImage(Image.open(icon_png))
        app.iconphoto(False, icon)
    except:
        pass

if os.path.exists(icon_ico):
    try:
        app.iconbitmap(icon_ico)
    except:
        pass


HACKER_BG = "#0a0a0a" 
HACKER_FG = "#00ff00" 
HACKER_FRAME_BG = "#111111"  
HACKER_BUTTON_BG = "#003300" 
HACKER_BUTTON_HOVER = "#006600" 
HACKER_BORDER = "#00ff00"
HACKER_TEXTBOX_BG = "#000000"  

app.configure(fg_color=HACKER_BG)

title_font = ("Courier New", 22, "bold")
label_font = ("Consolas", 12)
button_font = ("Consolas", 13, "bold")
log_font = ("Courier New", 9)

folder_var = ctk.StringVar()
password_var = ctk.StringVar()
mode_var = ctk.StringVar(value="encrypt")


def choose_folder():
    path = filedialog.askdirectory()
    if path:
        folder_var.set(path)


def start_process():
    folder = folder_var.get()
    password = password_var.get()
    mode = mode_var.get()

    if not folder:
        messagebox.showerror("Error," "Choose the folder path first")
        return

    if not password:
        messagebox.showerror("Error," "Enter password")
        return

    if len(password) < 8:
        messagebox.showwarning("Warning", "Password is too short (minimum 8 characters)")
        return

    if not os.path.exists(folder):
        messagebox.showerror("Error", "Folder not found")
        return

    log_box.configure(state="normal")
    log_box.delete("0.0", "end")
    log_box.configure(state="disabled")

    def log(msg):
        log_box.configure(state="normal")
        log_box.insert("end", msg + "\n")
        log_box.see("end")
        log_box.configure(state="disabled")
        app.update()

    if mode == "encrypt":
        if not messagebox.askyesno("Warning," "Original files will be deleted after successful encryption.\nDo you want to continue?"):
            return
        log(">>> Start the encryption process...")
        log(">>> " + "=" * 50)
        log("[*] Use PBKDF2 (600K) + AES-GCM")
        processed, failed = process_folder(folder, password, "encrypt", log)
        log(">>> " + "=" * 50)
        log(f">>> Result: ✔ {processed} | ✗ {failed}")
        log(">>> The decryption process is complete.")
        
    else:
        log(">>> Start the encryption process...")
        log(">>> " + "=" * 50)
        log("[**] Use PBKDF2 (600K) + AES-GCM")
        processed, failed = process_folder(folder, password, "decrypt", log)
        log(">>> " + "=" * 50)
        log(f">>> Result: ✔ {processed} | ✗ {failed}")
        log(">>> The decryption process is complete.")


title_frame = ctk.CTkFrame(app, fg_color=HACKER_BG, border_width=0)
title_frame.pack(pady=5)

title_label = ctk.CTkLabel(
    title_frame, 
    text="╔══════════════════════════════════════╗\n"
         "  LOCK-0 v1.0.0 - ENCRYPTION\n"
         "  PBKDF2-600K + AES-256-GCM\n"
         "╚══════════════════════════════════════╝",
    font=title_font,
    text_color=HACKER_FG
)
title_label.pack()

main_frame = ctk.CTkFrame(
    app, 
    fg_color=HACKER_FRAME_BG, 
    border_color=HACKER_BORDER, 
    border_width=2,
    corner_radius=0
)
main_frame.pack(pady=1, padx=1, fill="both", expand=True)

folder_frame = ctk.CTkFrame(
    main_frame, 
    fg_color=HACKER_FRAME_BG, 
    border_color=HACKER_BORDER, 
    border_width=1,
    corner_radius=0
)
folder_frame.pack(pady=5, padx=1, fill="x")

ctk.CTkLabel(
    folder_frame, 
    text="[1] Select the folder:", 
    font=label_font,
    text_color=HACKER_FG
).pack(anchor="w", padx=10, pady=5)

folder_inner_frame = ctk.CTkFrame(folder_frame, fg_color=HACKER_FRAME_BG, border_width=0)
folder_inner_frame.pack(pady=5, padx=10, fill="x")

folder_entry = ctk.CTkEntry(
    folder_inner_frame, 
    textvariable=folder_var, 
    width=400,
    font=label_font,
    fg_color="#0a0a0a",
    border_color=HACKER_BORDER,
    text_color=HACKER_FG,
    corner_radius=0
)
folder_entry.pack(side="left", padx=5)

browse_btn = ctk.CTkButton(
    folder_inner_frame, 
    text="Browse", 
    width=100,
    font=button_font,
    command=choose_folder,
    fg_color=HACKER_BUTTON_BG,
    hover_color=HACKER_BUTTON_HOVER,
    text_color=HACKER_FG,
    border_color=HACKER_BORDER,
    border_width=1,
    corner_radius=0
)
browse_btn.pack(side="left", padx=5)

password_frame = ctk.CTkFrame(
    main_frame, 
    fg_color=HACKER_FRAME_BG, 
    border_color=HACKER_BORDER, 
    border_width=1,
    corner_radius=0
)
password_frame.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(
    password_frame, 
    text="[2] Enter the password (8+ characters):", 
    font=label_font,
    text_color=HACKER_FG
).pack(anchor="w", padx=10, pady=5)

password_entry = ctk.CTkEntry(
    password_frame, 
    textvariable=password_var, 
    show="•",
    font=label_font,
    fg_color="#0a0a0a",
    border_color=HACKER_BORDER,
    text_color=HACKER_FG,
    corner_radius=0
)
password_entry.pack(pady=5, padx=10, fill="x")

mode_frame = ctk.CTkFrame(
    main_frame, 
    fg_color=HACKER_FRAME_BG, 
    border_color=HACKER_BORDER, 
    border_width=1,
    corner_radius=0
)
mode_frame.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(
    mode_frame, 
    text="[3] Select the operation:", 
    font=label_font,
    text_color=HACKER_FG
).pack(anchor="w", padx=10, pady=5)

mode_inner_frame = ctk.CTkFrame(mode_frame, fg_color=HACKER_FRAME_BG, border_width=0)
mode_inner_frame.pack(pady=5, padx=10)

encrypt_radio = ctk.CTkRadioButton(
    mode_inner_frame,
    text="File encryption",
    variable=mode_var,
    value="encrypt",
    font=label_font,
    fg_color=HACKER_FG,
    border_color=HACKER_FG,
    text_color=HACKER_FG,
    hover_color="#00cc00",
    corner_radius=0
)
encrypt_radio.pack(side="left", padx=20)

decrypt_radio = ctk.CTkRadioButton(
    mode_inner_frame,
    text="decryption",
    variable=mode_var,
    value="decrypt",
    font=label_font,
    fg_color=HACKER_FG,
    border_color=HACKER_FG,
    text_color=HACKER_FG,
    hover_color="#00cc00",
    corner_radius=0
)
decrypt_radio.pack(side="left", padx=20)

start_btn = ctk.CTkButton(
    main_frame, 
    text=">>> Start the process <<<", 
    fg_color=HACKER_BUTTON_BG, 
    hover_color=HACKER_BUTTON_HOVER,
    font=("Consolas", 14, "bold"), 
    height=35,
    command=start_process,
    border_color=HACKER_BORDER,
    border_width=2,
    text_color=HACKER_FG,
    corner_radius=0
)
start_btn.pack(pady=2)

log_frame = ctk.CTkFrame(
    main_frame, 
    fg_color=HACKER_FRAME_BG, 
    border_color=HACKER_BORDER, 
    border_width=1,
    corner_radius=0
)
log_frame.pack(pady=10, padx=20, fill="both", expand=True)

ctk.CTkLabel(
    log_frame, 
    text="[4] Operations log:", 
    font=label_font,
    text_color=HACKER_FG
).pack(anchor="w", padx=10, pady=5)

log_box = ctk.CTkTextbox(
    log_frame, 
    width=440, 
    height=100, 
    font=log_font,
    fg_color=HACKER_TEXTBOX_BG,
    text_color=HACKER_FG,
    border_color=HACKER_BORDER,
    border_width=2,
    corner_radius=0
)
log_box.pack(pady=5, padx=10, fill="both", expand=True)
log_box.configure(state="disabled")


status_frame = ctk.CTkFrame(app, fg_color=HACKER_BG, border_width=0)
status_frame.pack(pady=5)

status_label = ctk.CTkLabel(
    status_frame, 
    text=" Encryption   |   Decryption   |   Security 100% ",
    font=("Consolas", 10),
    text_color="#00ff00"
)
status_label.pack()

features_label = ctk.CTkLabel(
    app, 
    text="✓ PBKDF2 600K Iterations  |  ✓ AES-256-GCM  |  ✓ Secure Deletion  |  ✓ v1.0.0",
    font=("Consolas", 9),
    text_color="#00aa00"
)
features_label.pack(pady=2)

version_label = ctk.CTkLabel(
    app, 
    text="© 2026 LOCK-0 ENCRYPTION SUITE v1.0.0",
    font=("Consolas", 11),
    text_color="#E4E7E1"
)
version_label.pack(pady=2)

app.mainloop()