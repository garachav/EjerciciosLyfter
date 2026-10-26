import menu,actions,data

def main():
    student_list=[]
    while True:
        user_option= menu.operation()
        if user_option==1:
            student_data= actions.student_info()
            actions.add_student(student_data,student_list)
            
        elif user_option==2:
            stud_delete_info=actions.student_delete_info()
            actions.delete_student(stud_delete_info,student_list)
            
        elif user_option==3:
            actions.see_current_students(student_list)
            
        elif user_option==4:
            actions.see_failed_students(student_list)
            
        elif user_option==5:
            avg_students=actions.avg_dicc(student_list)
            actions.see_best_average_grades(avg_students)
            
        elif user_option==6:
            avg_students=actions.avg_dicc(student_list)
            actions.see_all_average_grades(avg_students)
        
        elif user_option==7:
            student_list=data.import_data_csv('data.csv',student_list)
                        
        elif user_option==8:
            data.export_data_csv('data.csv',student_list)
        else:
            print("Adiós. ")
            break
        
if __name__ == '__main__':
    main()