from tkinter import *
from tkinter import filedialog,messagebox

from sklearn.metrics.classification import accuracy_score

feature = []
accuracy = 0
extract_time = 0
training_time = 0

def browse():
    global file_name,import_directory
    file_name = filedialog.askdirectory(title="Pilih folder dataset")
    import_directory.delete(0,'end')
    import_directory.insert(0, file_name)

def extract():
    global feature, extract_time, extraction_time_entry
    from feature_extraction import mfcc
    mfcc_obj = mfcc(import_directory.get())
    feature, extract_time = mfcc_obj.extract()
    extraction_time_entry.delete(0, 'end')
    extraction_time_entry.insert(END,str(extract_time))

def train_and_test():
    global feature, training_time, accuracy
    if feature == []:
        return
    from classification import svm_classsifier
    classifier = svm_classsifier(feature)
    accuracy, training_time, hype, angry, relax, gloom, fold = classifier.train_and_test(int(trim_param_entry.get()),
                                                        float(svm_param_gamma_entry.get()),
                                                        float(svm_param_C_entry.get()))
    test_acc_entry.delete(0,'end')
    test_time_entry.delete(0,'end')
    test_fold_entry.delete(0,'end')
    hype_entry.delete(0,'end')
    relax_entry.delete(0, 'end')
    angry_entry.delete(0, 'end')
    gloom_entry.delete(0, 'end')
    test_acc_entry.insert(END, str(accuracy))
    test_time_entry.insert(END, str(training_time))
    test_fold_entry.insert(END, str(fold))
    hype_entry.insert(END,str(hype))
    relax_entry.insert(END, str(relax))
    angry_entry.insert(END, str(angry))
    gloom_entry.insert(END, str(gloom))

root= Tk()
root.title("Klasifikasi Emosi EEG")
window = Frame(root)
window.pack()

init_frame = Frame(window)
init_frame.pack(side=TOP)

folder_frame = Frame(init_frame)
folder_frame.pack(padx=0, pady=0, side=LEFT)
import_label = Label(folder_frame, text="Pilih folder dataset:")
import_label.pack(side=LEFT)
import_directory = Entry(folder_frame)
import_directory.insert(END, 'Directory dataset')
import_directory.pack(side=LEFT,padx=2)
browse_directory = Button(folder_frame, text="Browse", command=browse)
browse_directory.pack(side=LEFT)

svm_trim = Frame(init_frame)
svm_trim.pack(side=TOP)

trim_param = Frame(svm_trim)
trim_param.pack(padx=20, pady=20)
trim_param_label = Label(trim_param, text="Pemotongan (0-12)")
trim_param_label.pack(side=TOP)
trim_param_entry = Entry(trim_param)
trim_param_entry.pack(side=LEFT,padx=20)

svm_param_gamma = Frame(svm_trim)
svm_param_gamma.pack(padx=20, pady=20)
svm_param_label = Label(svm_param_gamma, text="SVM Gamma")
svm_param_label.pack(side=TOP)
svm_param_gamma_entry = Entry(svm_param_gamma)
svm_param_gamma_entry.pack(side=LEFT,padx=20)

svm_param_C = Frame(svm_trim)
svm_param_C.pack(padx=20, pady=20)
svm_param_label = Label(svm_param_C, text="SVM C")
svm_param_label.pack(side=TOP)
svm_param_C_entry = Entry(svm_param_C)
svm_param_C_entry.pack(side=LEFT,padx=20)

extraction_frame = Frame(window)
extraction_frame.pack(padx=20, pady=20, side=TOP)
start_extract_btn = Button(extraction_frame, text="Mulai Ekstraksi Fitur",command=extract)
start_extract_btn.pack(side=LEFT,padx=5, pady=5)
extraction_time_label = Label(extraction_frame, text="Waktu Ekstraksi Fitur")
extraction_time_label.pack(side=LEFT,padx=5, pady=5)
extraction_time_entry = Entry(extraction_frame)
extraction_time_entry.pack(side=LEFT,padx=5, pady=5)

training_frame = Frame(window)
training_frame.pack(padx=20, pady=20, side=TOP)
start_train_btn = Button(training_frame, text="Mulai Training dan Testing",command=train_and_test)
start_train_btn.pack(side=LEFT)

result_frame = Frame(window)
result_frame.pack(padx=20, pady=20, side=TOP)
training_time_label = Label(result_frame, text="Waktu Training")
training_time_label.pack(side=LEFT,padx=5, pady=5)
test_time_entry = Entry(result_frame)
test_time_entry.pack(side=LEFT,padx=5, pady=5)
test_acc_label = Label(result_frame, text="Akurasi Testing")
test_acc_label.pack(side=LEFT,padx=5, pady=5)
test_acc_entry = Entry(result_frame)
test_acc_entry.pack(side=LEFT,padx=5, pady=5)
test_fold_label = Label(result_frame, text="Fold ke-")
test_fold_label.pack(side=LEFT,padx=5, pady=5)
test_fold_entry = Entry(result_frame)
test_fold_entry.pack(side=LEFT,padx=5, pady=5)

emotion_count_header = Frame(window)
emotion_count_header.pack(padx=20,pady=20,side=TOP)
jml_predict = Label(emotion_count_header,text = 'Jumlah Prediksi Setiap Kelas:')
jml_predict.pack(side = BOTTOM, padx = 5, pady = 5)

emotion_count = Frame(window)
emotion_count.pack(padx=20,pady=20)
hype_label = Label(emotion_count,text = "Hype: ")
hype_label.pack(side=LEFT, padx = 5, pady = 5)
hype_entry = Entry(emotion_count)
hype_entry.pack(side = LEFT, padx = 5, pady = 5)
relax_label = Label(emotion_count,text = "Relax: ")
relax_label.pack(side = LEFT, padx = 5, pady = 5)
relax_entry = Entry(emotion_count)
relax_entry.pack(side = LEFT, padx = 5, pady = 5)
angry_label = Label(emotion_count, text = "Angry: ")
angry_label.pack(side = LEFT, padx = 5, pady = 5)
angry_entry = Entry(emotion_count)
angry_entry.pack(side = LEFT, padx = 5, pady = 5)
gloom_label = Label(emotion_count,text = "Gloom:")
gloom_label.pack(side = LEFT, padx = 5, pady = 5)
gloom_entry = Entry(emotion_count)
gloom_entry.pack(side = LEFT, padx = 5, pady = 5)

root.mainloop()