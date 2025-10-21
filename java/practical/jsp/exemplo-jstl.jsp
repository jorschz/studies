<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1" %>
<!-- 
<%@ page import="java.io.*,java.util.*,java.sql*"%>
<%@ page import="javax.servlet.http.*,javax.servlet.*"%> 
<%@ taglib uri="http://java.sun.com/jsp/jstl/sql" prefix="sql"%>
-->
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>


<!DOCTYPE html>
<html>
<head>
    <meta charset="ISO-8859-1">
    <title>Utilizando o JSTL</title>
</head>
<body>

    <!-- <div>
    <h1> Demonstracao - JSTL e Formatacao</h1>
    <p><strong>Data/Hora do Servidor:</strong> <%= new java.util.Date() %></p>

    <hr>
        <h2>Demonstracao SQL</h2>

    <sql:setDataSource var="snapshot" driver="com.mysql.jdbc.Driver"
        url="jdbc:mysql://localhot:3306/agenda?useSSL=false&serverTimezone=UTC"
        user="root" password="root"/>
    <sql:query dataSource="${snapshot}" var="result">
        SELECT * FROM agenda.contato
    </sql:query>

    <table border="1" width="100%">
        <tr>
            <th>Emp ID</th>
            <th>Nome</th>
            <th>E-mail</th>
        </tr>

        <c:forEach var="row" items="${result.rows}">
            <tr>
                <td><c:out value="${row.Id}"/></td>
                <td><c:out value="${row.nome}"/></td>
                <td><c:out value="${row.email}"/></td>
            </tr>
        </c:forEach>
    </table>
    </div> -->

    <hr>

    <div>
        <h2>Formatacao Numerica</h2>

        <c:set var="balance" value="120000.2309" />
        <c:set var="porc" value="0.10" />
        <c:set var="numeroGrande" value="1234567.8912"/>
        
        <p><strong>Moeda local (BRL):</strong>
            <fmt:formatNumber value="${balance}" type="currency" /></p>
        
        <p><strong>Porcentagem (10%):</strong>
            <fmt:formatNumber type="percent" value="${porc}" /></p>

        <p><strong>Notacao exponencial:</strong>
           <fmt:formatNumber type="number" pattern="###.###E0" value="${balance}" /></p>
        
        <p><strong>Numero com agrupamento:</strong>
            <fmt:formatNumber value="${numeroGrande}" groupingUsed="true" /></p>
             
        <p><strong>Moeda americana (USD):</strong>
           <fmt:setLocale value="en_US" />
           <fmt:formatNumber value="${balance}" type="currency" /></p>
        
        <p><strong>Moeda europeia (EUR)</strong>
            <fmt:setLocale value="de_DE"/>
            <fmt:formatNumber value="${balance}" type="currency"/></p>
    </div>

    <hr>
    
    <div>
        <h2>Formatacao de Datas e Horas</h2>

        <c:set var="now" value="<%=new java.util.Date()%>"/>



        <p><strong>Data original: </strong> <c:out value="${now}" /></p>
        <p><strong>Apenas hora:</strong> <fmt:formatDate type="time" value="${now}"/></p>
        <p><strong>Apenas data:</strong><fmt:formatDate type="date" value="${now}" /></p>
        <p><strong>Data e hora:</strong> <fmt:formatDate type="both" value="${now}" /></p>
        <p><strong>Data longa:</strong> <fmt:formatDate type="date" dateStyle="long" value="${now}" /></p>
        <p><strong>Formato customizado (dd-MM-yyyy)</strong>
           <fmt:formatDate pattern="dd-MM-yyyy" value="${now}" /></p>
        <p><strong>Formato customizado (dd/MM/yyyy HH:mm):</strong>
            <fmt:formatDate pattern="dd/MM/yyyy HH:mm" value="${now}" /></p>
    </div>

    <hr>
    
    <div>
        <h2>Logica Condicional com Salarios</h2>

        <c:set var="salary" scope="session" value="${2000*2}" />
        <c:set var="salarioMinimo" value="1412.00" />

        <p><strong>Salario atual:</strong>
            <fmt:formatNumber value="${salary}" type="currency" /></p>
        <p><strong>Salario minimo:</strong>
            <fmt:formatNumber value="${salarioMinimo}" type="currency" /></p>

        <c:choose>
            <c:when test="${salary <= 0}">
                <p style="color:red; font-weight: bold;"> Salario muito baixo para sobreviver</p>
            </c:when>
            <c:when test="${salary < salarioMinimo}">
                <p style="color:orange; font-weight: bold;">Salario abaixo do minimo</p>
            </c:when>
            <c:when test="${salary >= salarioMinimo && salary <= 3000}">
                <p style="color:blue; font-weight:bold;">Salario dentro da media</p>
            </c:when>
            <c:when test="${salary > 3000 && salary <= 10000}">
                <p style="color:green; font-weight: bold;">Salario acima da media!</p>
            </c:when>
            <c:otherwise>
                <p style="color:purple; font-weight: bold;">Salario excelente!</p>
            </c:otherwise>
        </c:choose>
    </div>
    <hr>
    <footer>
        <p><em>Página gerada em: <fmt:formatDate type="both" dateStyle="full" timeStyle="full" value="${now}" /></em></p>
    </footer>
</body>
</html>