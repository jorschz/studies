package controller;

import java.io.IOException;
// import java.sql.Connection;
// import java.sql.PreparedStatement;
import java.util.List;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import model.Student;
import dao.StudentDbUtil;

@WebServlet("/StudentControllerServlet")
public class StudentControllerServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    private StudentDbUtil studentDbUtil;

    @Override
    public void init() throws ServletException {
        super.init();
        // Inicializa o StudentDbUtil
        studentDbUtil = new StudentDbUtil();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // lista os estudantes utilizando o pattern MVC
        try {
            // listStudents(request, response);

            // Verificar o valor do parâmetro "command"
            String command = request.getParameter("command");

            // escolher a opção correta da operação
            if (command == null) {
                command = "LIST";
            }

            switch (command) {
                case "LIST":
                    listStudents(request, response);
                    break;
                case "ADD":
                    addStudent(request, response);
                    break;
                case "LOAD":
                    loadStudent(request, response);
                    break;
                case "UPDATE":
                    updateStudent(request, response);
                    break;
                case "DELETE":
                    deleteStudent(request, response);
                    break;
                default:
                    listStudents(request, response);

            }
        } catch (Exception e) {
            throw new ServletException(e);
        }
    }

    private void addStudent(HttpServletRequest request, HttpServletResponse response)
            throws Exception {
        // recuperar as informações enviadas
        String firstName = request.getParameter("firstName");
        String lastName = request.getParameter("lastName");
        String email = request.getParameter("email");

        // criar u mnovo objeto de estudante
        Student student = new Student(firstName, lastName, email);

        // gravar na base
        studentDbUtil.addStudent(student);

        // voltar para a lista de estudantes
        listStudents(request, response);

    }

    private void listStudents(HttpServletRequest request, HttpServletResponse response)
            throws Exception {

        // recuperar estudantes do banco de dados
        List<Student> students = studentDbUtil.getStudent();

        // adicionar os dados do request
        request.setAttribute("STUDENTS_LIST", students);

        // enviar para a página JSP (view)
        RequestDispatcher dispatcher = request.getRequestDispatcher("/list-student.jsp");
        dispatcher.forward(request, response);
    }

    private void loadStudent(HttpServletRequest request, HttpServletResponse response) throws Exception {
        // ler o id do estudante na base
        String studentId = request.getParameter("studentId");

        int id = Integer.parseInt(studentId);

        // recuperar os dados do estudante com base no id informado
        Student student = studentDbUtil.getStudent(id);

        // setar o objeto no request
        request.setAttribute("THE_STUDENT", student);

        // enviar para pagina de alteração
        RequestDispatcher dispatcher = request.getRequestDispatcher("/add-student-form.jsp");
        dispatcher.forward(request, response);
    }

    private void updateStudent(HttpServletRequest request, HttpServletResponse response) throws Exception {
        // let a informação
        int id = Integer.parseInt(request.getParameter("studentId"));
        String firstName = request.getParameter("firstName");
        String lastName = request.getParameter("lastName");
        String email = request.getParameter("email");

        // Criar um objeto de students
        Student student = new Student(id, firstName, lastName, email);

        // alterar os dados na base
        studentDbUtil.updateStudent(student);

        // voltar para alista de estudantes
        listStudents(request, response);

    }

    private void deleteStudent(HttpServletRequest request, HttpServletResponse response) throws Exception{
        
        int id = Integer.parseInt(request.getParameter("studentId"));
        studentDbUtil.deleteStudent(id);
        listStudents(request, response);
    }

}