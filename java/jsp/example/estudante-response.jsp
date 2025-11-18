<%@page import="java.util.*"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1" %>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="ISO-8859-1">
        <title>Confirmacao do Estudante</title>
    </head>
    <body>
        <p><strong>Aluno</strong> <%=request.getParameter("nome")%></p>
        <p><strong>RGM</strong> <%=request.getParameter("rgm")%><p>
        <p align="center">
            Ultima atualizacao:
            <%
                Calendar calendar = new GregorianCalendar();

                String am_pm;
                int hour = calendar.get(Calendar.HOUR);
                int minute = calendar.get(Calendar.MINUTE);
                int second = calendar.get(Calendar.SECOND);

                if(calendar.get(Calendar.AM_PM)==0){
                    am_pm = "AM";
                }else{
                    am_pm = "PM";
                }

                String CT = hour+":"+minute+":"+second+ " " + am_pm;
                
                out.print(CT);
            %>
        </p>
    </body>
</html>

