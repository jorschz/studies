    <%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
    <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="ISO-8859-1">
            <title>add-student-form</title>
        </head>
        <body>
            <div id="wrapper">
                <div id="header">
                    <h2>Lista Alunos</h2>
                </div>
            </div>

            <div id="container">
                <h3>Adicionar Estudante</h3>
                <form action="${pageContext.request.contextPath}/StudentControllerServlet" method="GET">
                    <input type="hidden" name="command" value="ADD" />
                    <input type="hidden" name="studentId" value="${THE_STUDENT.id}"/>
                
                    <table>
                        <tbody>
                            <tr>
                                <td><label>First name:</label></td>
                                <td><input type="text" name="firstName" 
                                value ="${THE_STUDENT.firstName}"/></td>
                            </tr>

                            <tr>
                                <td><label>Last name:</label></td>
                                <td><input type="text" name="lastName"
                                value ="${THE_STUDENT.lastName}"/></td>
                            </tr>

                            <tr>
                                <td><label>Email:</label></td>
                                <td><input type="text" name="email"
                                value ="${THE_STUDENT.email}"/></td>
                            </tr>

                            <tr>
                                <td><label></label></td>
                                <td><input type="submit" value="Save"/></td>
                            </tr>
                            
                        </tbody>
                    </table>
                </form>
            </div>
        </body>
    </html>