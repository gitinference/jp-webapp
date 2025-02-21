import "../../../styles/JP-544-qtr.css";

function JP_544_qtr() {
  return (
    <>
  <meta charSet="UTF-8" />
  <title>JP-544 Información para la Balanza de Pagos</title>
  {/* Header */}
  <section className="header">
    <table>
      <tbody>
        <tr>
          <td id="header_left">
            JP-544
            <br />
            Rev. Jul. 17
            <br />
            Centro Gubernamental Roberto Sánchez Vilella
            <br />
            Apartado 41119
            <br />
            San Juan, Puerto Rico 00940
            <br />
          </td>
          <td id="header_center">
            <img
              src="src/assets/JP_poster.jpg"
              alt="Logo Junta Planificación"
              id="header_image"
            />
            <br />
            <h3>
              INFORMACION PARA LA BALANZA DE PAGOS DE PUERTO RICO: AÑO FISCAL
            </h3>
            <br />
            <div className='dropdown'>
              <select id="quater_select" name="dropdown_fiscal_year">
                <option value="">Select Trimester</option>
                <option value="Q1-(Jan-Mar)">Q1-(Jan-Mar)</option>
                <option value="Q2-(Apr-Jun)">Q2-(Apr-Jun)</option>
                <option value="Q3-(Jul-Sep)">Q3-(Jul-Sep)</option>
                <option value="Q4-(Oct-Dec)">Q4-(Oct-Dec)</option>
              </select>
              <input
                type="number"
                id="year"
                name="bonds_year_left"
                min={1000}
                max={9999}
                placeholder="Year"
                required
              />
            </div>
          </td>
          <td id="header_right">
            Junta de Planificación de Puerto Rico
            <br />
            Programa de Planificación Económica y Social
            <br />
            Subprograma de Análisis Económico
            <br />
          </td>
        </tr>
      </tbody>
    </table>
  </section>
  <main>
    <form method="POST" action="{% url 'web_app:JP-544-qtr' %}">
      <section className="divider-container">
        <table>
          <tbody>
            <tr>
              <th colSpan={2}>
                <h3>
                  A- Donaciones recibidas de instituciones privadas del exterior
                  y/u organizaciones internacionales:
                </h3>
              </th>
              <th colSpan={1}>Recibos</th>
            </tr>
            {/* Line 1 */}
            <tr></tr>
            <tr>
              <th colSpan={1}>
                Institución privada u organización que la envía
              </th>
              <th colSpan={1}>Propósito</th>
              <th colSpan={1}>En miles de dólares</th>
            </tr>
            {/* Line 2 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion1"
                  placeholder="Institución"
                  required
                />
              </td>
              <td>
                <input
                  type="text"
                  name="proposito1"
                  placeholder="Propósito"
                  required
                />
              </td>
              <td>
                <input
                  type="number"
                  name="dolares1"
                  placeholder="$"
                  required
                />
              </td>
            </tr>
            {/* Line 3 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion2"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito2" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares2" placeholder="$" />
              </td>
            </tr>
            {/* Line 4 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion3"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito3" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares3" placeholder="$" />
              </td>
            </tr>
            {/* Line 5 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion4"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito4" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares4" placeholder="$" />
              </td>
            </tr>
            {/* Line 6 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion5"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito5" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares5" placeholder="$" />
              </td>
            </tr>
            {/* Line 7 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion6"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito6" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares6" placeholder="$" />
              </td>
            </tr>
            {/* Line 8 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion7"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito7" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares7" placeholder="$" />
              </td>
            </tr>
            {/* Line 9 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion8"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito8" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares8" placeholder="$" />
              </td>
            </tr>
            {/* Line 10 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion9"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito9" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares9" placeholder="$" />
              </td>
            </tr>
            {/* Line 11 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion10"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito10" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares10" placeholder="$" />
              </td>
            </tr>
            {/* Line 12 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion11"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito11" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares11" placeholder="$" />
              </td>
            </tr>
            {/* Line 13 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion12"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito12" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares12" placeholder="$" />
              </td>
            </tr>
            {/* Line 14 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion13"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito13" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares13" placeholder="$" />
              </td>
            </tr>
            {/* Line 15 */}
            <tr>
              <td>
                <input
                  type="text"
                  name="institucion14"
                  placeholder="Institución"
                />
              </td>
              <td>
                <input type="text" name="proposito14" placeholder="Propósito" />
              </td>
              <td>
                <input type="number" name="dolares14" placeholder="$" />
              </td>
            </tr>
          </tbody>
        </table>
      </section>
      <br />
    </form>
  </main>
  <br />
  <br />
  <main>
    {/* Segunda Tabla */}
    <section className="divider-container">
      <h3>B- Pagos a personas o firmas en el exterior:</h3>
      <table>
        {/* Line 1 */}
        <tbody>
          <tr>
            <th rowSpan={2}>Concepto</th>
            <th rowSpan={2}>Pagos en miles de dólares</th>
          </tr>
          {/* Line 2 */}
          <tr></tr>
          <tr>
            <td>
              1. Por gastos de operación de las oficinas situadas fuera de
              Puerto Rico, total
            </td>
            <td>
              <input type="number" name="operation_expenses" placeholder="$" />
            </td>
          </tr>
          {/* Line 3 */}
          <tr>
            <td> a. Sueldos y jornales</td>
            <td>
              <input type="number" name="salary" placeholder="$" />
            </td>
          </tr>
          {/* Line 4 */}
          <tr>
            <td>
               b. Aportación patronal al Seguro Social, Seguro por Desempleo,
              Sistema de Retiro, a fondos de uniones obreras y otros beneficios
              marginales.
              <br />
            </td>
            <td>
              <input
                type="number"
                name="SS_SD_SR_beneficios_marginales"
                placeholder="$"
              />
            </td>
          </tr>
          {/* Line 5 */}
          <tr>
            <td> c. Servicios profesionales y consultivos</td>
            <td>
              <input
                type="number"
                name="servicios_profecionales_c"
                placeholder="$"
              />
            </td>
          </tr>
          {/* Line 6 */}
          <tr>
            <td> d. Intereses</td>
            <td>
              <input type="number" name="intereses" placeholder="$" />
            </td>
          </tr>
          {/* Line 7 */}
          <tr>
            <td> e. Otros gastos</td>
            <td>
              <input type="number" name="other_gastos" placeholder="$" />
            </td>
          </tr>
          {/* Line 8 */}
          <tr>
            <td>
              <br />
            </td>
            <td>
              <br />
            </td>
          </tr>
          {/* Line 9 */}
          <tr>
            <td>2. A personas o firmas en el exterior, Total 1/</td>
            <td>
              <input type="number" name="to_people" placeholder="$" />
            </td>
          </tr>
          {/* Line 10 */}
          <tr>
            <td>  a. Servicios profesionales, consultivos y honorarios</td>
            <td>
              <input
                type="number"
                name="servicios_profecionales_a"
                placeholder="$"
              />
            </td>
          </tr>
          {/* Line 11 */}
          <tr>
            <td>  b. Pensiones</td>
            <td>
              <input type="number" name="pension" placeholder="$" />
            </td>
          </tr>
          {/* Line 12 */}
          <tr>
            <td>  c. Otros gastos (especifique) 2/</td>
          </tr>
          {/* Line 13 */}
          <tr>
            <td>
              <input type="text" name="name_other_1" placeholder="Otros" />
            </td>
            <td>
              <input type="number" name="quantity_other_1" placeholder="$" />
            </td>
          </tr>
          {/* Line 14 */}
          <tr>
            <td>
              <input type="text" name="name_other_2" placeholder="Otros" />
            </td>
            <td>
              <input type="number" name="quantity_other_2" placeholder="$" />
            </td>
          </tr>
          {/* Line 15 */}
          <tr>
            <td>
              <input type="text" name="name_other_3" placeholder="Otros" />
            </td>
            <td>
              <input type="number" name="quantity_other_3" placeholder="$" />
            </td>
          </tr>
          {/* Line 16 */}
          <tr>
            <td>
              <input type="text" name="name_other_4" placeholder="Otros" />
            </td>
            <td>
              <input type="number" name="quantity_other_4" placeholder="$" />
            </td>
          </tr>
        </tbody>
      </table>
      1/ No incluya los pagos informados en las planillas de contribuciones
      retenidas en el origen.
      <br />
      2/ No incluya pagos por compra de materiales y equipos, fletes y otros
      gastos de transportació;
      <br />
      ni pago de intereses por deudas a corto largo plazo.
    </section>
    <div className="custom-line" />
    <div id="text_button" />
    <br />
    <br />
    <br />
    <br />
    <br />
    <section>
      <div className="big-box-bottom-left">
        <strong> Nombre de la Agencia :</strong>
        <input
          className="text-box space-between"
          name="agencia"
          placeholder="Agencia"
          required
        />
        <br />
        <strong> Preparado por :</strong>
        <input
          className="text-box space-between"
          name="prep"
          placeholder="Nombre"
          required
        />
        <br />
        <strong> Título o puesto :</strong>
        <input
          className="text-box space-between"
          name="titulo"
          placeholder="Título"
          required
        />
        <br />
        <strong> Teléfono :</strong>
        <br />
        <input
          className="text-box space-between"
          name="telefono"
          placeholder="123-456-7890"
          required
        />
        <br />
        <strong> Fecha :</strong>
        <input
          className="text-box space-between"
          name="fecha"
          placeholder="MM/DD/YYYY"
          required
        />
        <br />
      </div>
    </section>
    <section className="submit-button-container">
      <input type="submit" defaultValue="SUBMIT" className="submit-button" />
    </section>
  </main>
</>
    
  );
}

export default JP_544_qtr;