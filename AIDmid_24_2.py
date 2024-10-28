import streamlit as st
import pandas as pd

exam_title = "2024 Fall Artificial Intelligence Design"
fname = "AID_Midterm_Grading.xlsx"
solution = '''
## Solution
#### 1. (10p - 2p each)
    (a) T
    (b) T
    (c) F
    (d) T
    (e) F

#### 2. (12p - 3p each)
    (a) Untracked
    (b) Unmodified
    (c) Modified
    (d) Staged

#### 3. (8p)
    Var = "this is a variable"
    echo $Var

#### 4. (12p - 3p each)
    (a) Shell
    (b) Command Line Interface
    (c) pwd
    (d) printenv

#### 5. (12P)
    mkdir /mnt/data/WorkSpace
    cd /mnt/data/WorkSpace
    mkdir 2024
    cd 2024
    pwd
    cd ../..
    rm -r /mnt/data/WorkSpace

#### 6. (18p)
    (a) - 4p
    42
    (b) - 4p
    21
    (c) - 6p
    def border_one_2d(num):
        arr = np.zeros((num,num), dtype=int)
        arr[0,:]=1
        arr[-1,:]=1
        arr[:,0]=1
        arr[:,-1]=1
        return arr
    (d) - 4p
    [[5,6,8], [8,0,5], [10,3,12], [14,13,14]]

#### 7. (14p)
    (a) - 9p (3p each)
    (1) git branch my_branch
    (2) git add hello.txt
    (3) git commit -m "Modified hello.txt in my_branch"
    (b) - 5p
    "git clone" is about obtaining a new local copy of a repository.
    "git pull" is about updating an existing local copy
    with new commits from the remote repository.

#### 8. (8p - 4p each)
    (a) git log
    (b) git status

#### 9. (6p)
    Copyleft licenses require any derivative works to also be released under the same or
    a compatible open-source license, ensuring ongoing freedom to use, modify, and share.
    Permissive licenses, on the other hand, allow derivative works to be released under any terms,
    including proprietary ones, providing greater flexibility and fewer restrictions on how software
    can be used and redeistributed. '''

# Setup Title & Wide layout
st.set_page_config(page_title=exam_title, layout="wide")
st.markdown(
    """
    <style>
    textarea {
        font-size: 2rem !important;
    }
    input {
        font-size:1.5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Load the Excel data
df = pd.read_excel(fname, dtype={'Student ID': 'Int64', '1 - 10p': 'Int64', '2 - 12p': 'Int64', '3 - 8p': 'Int64'})

def get_student_data(student_id):
    """
    Fetch the data for a given student ID from the Excel file.
    
    Args:
    - student_id (int): The ID of the student.
    
    Returns:
    - pd.DataFrame or None: The data for the student if found, otherwise None.
    """
    student_data = df[df["e-mail"] == student_id]
    if len(student_data) > 0:
        return student_data
    else:
        return None

# Streamlit app layout and logic
st.title(exam_title)

# Get the student ID from the user
student_id = st.text_input("Enter your email", value='hwanheelee@cau.ac.kr')

# When the user provides a student ID, fetch and display the data
if student_id:
    data = get_student_data(student_id)
    
    if data is not None:
        to_show = data.set_index("e-mail")
        st.write("E-mail: ", to_show.index[0])
        s = to_show.style.format({"Expense": lambda x : '{:.4f}'.format(x)})
        st.dataframe(s, hide_index=True)
    else:
        st.write(f"No data found for email: {student_id}")
        
st.write(solution)
