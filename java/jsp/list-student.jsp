<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1" %>
    <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

        <!DOCTYPE html>
        <htmL>

        <head>
            <meta charset="ISO-8859-1">
            <title>List Students</title>
        
            <style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
    }

    table {
        border-collapse: collapse;
        width: 100%;
        margin-top: 20px;
    }

    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }

    th {
        background-color: #f2f2f2;
    }

    .add-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 15px;
        border: none;
        cursor: pointer;
        margin-bottom: 20px;
    }

    .add-button:hover {
        background-color: #45a049;
    }
</style>
        </head>

        <body>

            <div id="wrapper">
                <div id="header">
                    <h2>Lista de Aluno</h2>
                </div>

                <div id="content">
                    <input type="button" value="Add Student" class="add-button" onclick="addstudent()" />
                    <table border="1">
                        <tr>
                            <th>First Name</th>
                            <th> Last Name</th>
                            <th> Email</th>
                            <th> Action</th>
                        </tr>
                        <c:forEach var="tempStudent" items="${STUDENTS_LIST}">
                            <c:url var="tempLink" value="StudentControllerServlet">
                                <c:param name="command" value="LOAD" />
                                <c:param name="studentId" value="${tempStudent.id}" />
                            </c:url>

                            <c:url var="tempLinkDelete" value="StudentControllerServlet">
                                <c:param name="command" value="DELETE" />
                                <c:param name="studentId" value="${tempStudent.id}" />
                            </c:url>

                            <tr>
                                <td>${tempStudent.firstName}</td>
                                <td>${tempStudent.lastName}</td>
                                <td>${tempStudent.email}</td>
                                <td>
                                    <a href="${tempLink}">Update</a>
                                    <a href="${tempLinkDelete}" onclick="delstudent()">Delete</a>
                                </td>
                            </tr>
                        </c:forEach>
                    </table>
                </div>
            </div>
            <div>
                <script>
                    function addstudent() {
                        window.location.href = 'add-student-form.jsp';
                    }

                    function delstudent() {
                        return confirm('Tem certeza que deseja excluir este estudante?');
                    }
                </script>
            </div>
        </body>

        </htmL>