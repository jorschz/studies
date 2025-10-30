<%@ page contentType="text/html;charset=UTF-8" %>
<html>
<body>
    <h1>🎉 SUCESSO TOTAL! 🎉</h1>
    <p>Link simbólico funcionando perfeitamente!</p>
    <p>Data: <%= new java.util.Date() %></p>
    <p>URL: http://localhost:8080/jsp/teste-funcionamento.jsp</p>
    
    <h2>Teste Interativo:</h2>
    <form>
        <input type="text" name="mensagem" placeholder="Digite algo">
        <input type="submit" value="Testar">
    </form>
    
    <% if(request.getParameter("mensagem") != null) { %>
        <p>Você digitou: "<strong><%= request.getParameter("mensagem") %></strong>"</p>
    <% } %>
</body>
</html>
