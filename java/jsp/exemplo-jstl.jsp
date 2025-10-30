<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/sql" prefix="sql" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>

<fmt:setLocale value="pt_BR" scope="session"/>

<!DOCTYPE html>
<html>
<head>
    <meta charset="ISO-8859-1">
    <title>Utilizando o JSTL</title>
    <style>
    .cor{
        color:red;
    }
    table {
        border-collapse:collapse;
        width: 100%;
        margin: 20px 0;
    }
    th, td{
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
    }
    tr:nth-child(even){
        background-color:#f9f9f9;
    }
    </style>

</head>
<body>
    
    <h1> Demonstracao - JSTL e Formatacao</h1>
    <p><strong>Data/Hora do Servidor:</strong> <%= new java.util.Date() %></p>

    <hr>

    <div>
        <sql:setDataSource 
	        var="snapshot" 
            driver="com.mysql.cj.jdbc.Driver"
            url="jdbc:mysql://localhost:3306/agenda?useSSL=false&serverTimezone=UTC"
            user="jsp_user"
            password="jsp123"
        />  

        <sql:query dataSource="${snapshot}" var="result">
            select id, nome, email FROM contato
        </sql:query>

        <table border="1" width="100%">
            <tr>
                <th>Id Empregado</th>
                <th>Funcionario</th>
                <th>E-mail</th>
            </tr>
            <c:forEach var="registro" items="${result.rows}">
                <tr>
                    <td><c:out value="${registro.id}"/></td>
                    <td><c:out value="${registro.nome}"/></td>
                    <td><c:out value="${registro.email}"/></td>
                </tr>
            </c:forEach>
        </table>
        
    </div>

    <hr>

    <div>
        <h2>Formatacao Numerica</h2>

        <c:set var="balance" value="120000.2309" />
        <c:set var="porc" value="0.10" />
        <c:set var="numeroGrande" value="1234567.8912"/>
        
        <p><strong>Moeda Brasileira</strong>
            <fmt:formatNumber value="${balance}" type="currency"/></p>

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
            <fmt:formatNumber value="${balance}" type="currency" currencyCode="EUR"/></p>
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
        <fmt:parseNumber var="salarioMinimo" value="1412.00" type="number" />

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
    <div>
        <h2>Exemplo de integracao com JAVA</h2>
       <form action="estudante-response.jsp" method="POST">
            <p><strong>Nome: </strong><input type="text" name="nome" class="cor"/></p>
            <p><strong>RGM:</strong><input type="text"name="rgm"/></p>
            <p><input type="submit" value="Enviar!"/></p>
       </form> 
    </div>
    <hr>
    <footer>
        <p><em>Pagina gerada em: <fmt:formatDate type="both" dateStyle="full" timeStyle="full" value="${now}" /></em></p>
    </footer>
</body>
</html>