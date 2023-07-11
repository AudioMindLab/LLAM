---
headless: true # This file represents a page section.
weight: 10 # Order that this section will appear.
title: |
  In Progress

design:
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns: '1'
  # Add custom styles
  css_style:
  css_class:
---
<style>
  table {
    border-collapse: collapse;
  }

  th {
    background-color: #f2f2f2;
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }

  td {
    border: 1px solid #ddd;
    padding: 8px;
  }
</style>

<script>
    window.addEventListener('DOMContentLoaded', function() {
      var table = document.getElementById('myTable');
      var rows = table.getElementsByTagName('tr');
      var idCounter = 1;

      for (var i = 1; i < rows.length; i++) {
        var row = rows[i];
        var cells = row.getElementsByTagName('td');
        cells[0].innerText = idCounter;
        idCounter++;
      }
    });
</script>

<div align=center>
  <table id="myTable">
    <tr>
      <th>ID</th>
      <th>论文</th>
      <th>会议/期刊</th>
      <th>状态</th>
    </tr>
    <tr>
      <td>16</td>
      <td>luokaiyi</td>
      <td>ICTAI</td>
      <td>在投</td>
    </tr>
    <tr>
      <td>4</td>
      <td>sunaolan</td>
      <td>ICTAI</td>
      <td>interspeech拒稿 在投</td>
    </tr>
    <tr>
      <td>17</td>
      <td>dengyimin</td>
      <td>SPL/ICTAI</td>
      <td>interspeech拒稿 在投</td>
    </tr>
    <tr>
      <td>3</td>
      <td>dengyimin,liangziqi</td>
      <td>ICTAI</td>
      <td>ADMA拒稿 在投</td>
    </tr>
      <tr>
      <td>3</td>
      <td>liangziqi</td>
      <td>ICTAI</td>
      <td>在投</td>
    </tr>
    <tr>
      <td>9</td>
      <td>luokaiyi</td>
      <td>MM拒稿 iconip</td>
      <td>在投</td>
    </tr>
    <tr>
      <td>10</td>
      <td>联邦音频大模型</td>
      <td>智能系统学报</td>
      <td>在投</td>
    </tr>
    <tr>
      <td>14</td>
      <td>dengyimin</td>
      <td>MM</td>
      <td>acl拒稿 在投</td>
    </tr>
    <tr>
      <td>15</td>
      <td>dengyimin</td>
      <td>MM</td>
      <td>ijcai拒稿 在投</td>
    </tr>
    <tr>
      <td>5</td>
      <td>jishengpeng</td>
      <td>emnlp</td>
      <td>interspeech拒稿 在投</td>
    </tr>
    <tr>
      <td>6</td>
      <td>sunyifu</td>
      <td>EURASIP</td>
      <td>在投</td>
    </tr>
  </table>
</div>