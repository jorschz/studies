package controller;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(
    description = "Servlet de demonstração de criação", 
    urlPatterns = { "/HelloWorldServlet" }
)
public class HelloWorldServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    public HelloWorldServlet() {
        super();
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        // Configurar content type com encoding
        response.setContentType("text/html; charset=UTF-8");
        
        // Obter writer para escrever resposta
        PrintWriter out = response.getWriter();
        
        // Gerar HTML
        out.println("<!DOCTYPE html>");
        out.println("<html>");
        out.println("<head>");
        out.println("<title>Meu Primeiro Servlet</title>");
        out.println("</head>");
        out.println("<body>");
        out.println("<h2>Hello World do Servlet!</h2>");
        out.println("<hr>");
        out.println("<p>Data/hora no servidor: " + new java.util.Date() + "</p>");
        out.println("</body>");
        out.println("</html>");
        
        out.close();
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doGet(request, response);
    }
}