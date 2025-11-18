package dao;

import model.Student;

import javax.sql.DataSource;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class StudentDbUtil {

    private DataSource dataSource;

    // Construtor padrão - busca DataSource via JNDI
    public StudentDbUtil() {
        try {
            Context context = new InitialContext();
            dataSource = (DataSource) context.lookup("java:comp/env/jdbc/agenda");
        } catch (NamingException e) {
            e.printStackTrace();
            throw new RuntimeException("Erro ao encontrar DataSource: " + e.getMessage());
        }
    }

    // Construtor para testes
    public StudentDbUtil(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    // Método get students
    public List<Student> getStudent() throws Exception {

        List<Student> students = new ArrayList<>();

        Connection con = null;
        Statement stmt = null;
        ResultSet rs = null;

        try {
            // Passo 1: obter a conexão
            con = dataSource.getConnection();

            // Passo 2: criar o comando SQL
            String sql = "SELECT * FROM student ORDER BY last_name";
            stmt = con.createStatement();

            // Passo 3: executar o comando
            rs = stmt.executeQuery(sql);

            // Passo 4: processar o resultado
            while (rs.next()) {
                // recuperar a informação do resultset
                int id = rs.getInt("id");
                String firstName = rs.getString("first_name");
                String lastName = rs.getString("last_name");
                String email = rs.getString("email");

                // criar o objeto Student
                Student tempStudent = new Student(id, firstName, lastName, email);

                // adicionar à lista
                students.add(tempStudent);
            }

            return students;

        } finally {
            // Passo 5: fechar a conexão
            close(con, stmt, rs);
        }
    }

    public Student getStudent(int id) throws Exception {
        Connection con = null;
        PreparedStatement stmt = null;
        ResultSet rs = null;
        Student student = null;

        try {
            con = dataSource.getConnection();
            String sql = "SELECT * FROM student WHERE id=?";
            stmt = con.prepareStatement(sql);
            stmt.setInt(1, id);
            rs = stmt.executeQuery();

            if (rs.next()) {
                String firstName = rs.getString("first_name");
                String lastName = rs.getString("last_name");
                String email = rs.getString("email");
                student = new Student(id, firstName, lastName, email);
            }
            return student;
        } finally {
            close(con, stmt, rs);
        }
    }

    public void addStudent(Student student) throws Exception {
        // criar a instrução para gravar
        Connection con = null;
        PreparedStatement stmt = null;

        try {
            // configurar os valores dos estudantes
            con = dataSource.getConnection();

            String sql = "INSERT INTO student (FIRST_NAME, LAST_NAME, EMAIL) VALUES (?, ?, ?)";

            stmt = con.prepareStatement(sql);
            stmt.setString(1, student.getFirstName());
            stmt.setString(2, student.getLastName());
            stmt.setString(3, student.getEmail());

            // executar a instrução
            stmt.execute();
        } finally {
            // fechar os objetos
            close(con, stmt, null);
        }
    }

    // Método close - necessário para fechar recursos
    private void close(Connection con, Statement stmt, ResultSet rs) {
        try {
            if (rs != null) {
                rs.close();
            }
            if (stmt != null) {
                stmt.close();
            }
            if (con != null) {
                con.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void updateStudent(Student student) throws Exception {
        // criar a instruçõa para alterar
        Connection con = null;
        PreparedStatement stmt = null;

        try {
            // configurar os calores dos estudantes
            con = dataSource.getConnection();

            String sql = "UPDATE student SET FIRST_NAME = ?, LAST_NAME = ?, EMAIL = ? WHERE ID = ?";

            stmt = con.prepareStatement(sql);
            stmt.setString(1, student.getFirstName());
            stmt.setString(2, student.getLastName());
            stmt.setString(3, student.getEmail());
            stmt.setInt(4, student.getId());

            // executar a instrução
            stmt.execute();
        } finally {
            // fechar os objetos
            close(con, stmt, null);
        }
    }

    public void deleteStudent(int id) throws Exception {
        // criar a instrução para excluir
        Connection con = null;
        PreparedStatement stmt = null;

        try {
            // concetar no banco
            con = dataSource.getConnection();

            // configurar a instrução
            String sql = "DELETE FROM student WHERE ID = ?";

            // preparar a instrução
            stmt = con.prepareStatement(sql);

            // configurar os parametros
            stmt.setInt(1, id);

            // executar a instrução
            stmt.execute();
        } finally {
            // fecahr of objetos
            close(con, stmt, null);
        }
    }
}