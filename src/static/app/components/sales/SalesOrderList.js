class SalesOrderTable extends React.Component {

    constructor(props) {
        super(props);
        
        this.state = {
            rows: []
        };
    }

    componentDidMount() {
        $.getJSON('/sales/list')
        .then((rows) => {
            this.setState({ rows: rows });
        });
    }
    
    render() {
        return (
            <table className="table table-bordered">
                <thead>
                    <tr><th>Id</th><th>Remarks</th><th>Customer</th></tr>
                </thead>
                <tbody>
                {this.state.rows.map(row =>
                    <tr onClick={() => this.props.rowClicked(row)}>
                        <td><a href={"/sales/order/?id=" + row.id}>{row.id}</a></td>
                        <td>{row.remarks}</td>
                        <td>{row.customer_name}</td>
                    </tr>
                )}
                </tbody>
            </table>
        );
    }
}

    SalesOrderTable.propTypes = {
        rowClicked: React.PropTypes.func,
    };

class SalesOrderEdit extends React.Component {

    constructor(props) {
        super(props);
    
        this.state = {
            row : {}
        };
    }
    
    setData(row) {
    
        if (row.remarks === null)
            row.remarks = '';
    
        this.setState({row: row});
    }
    
    render() {
        return (
            <div>
                Id: <input type="text" value={this.state.row.id} />
                Remarks: <input type="text" value={this.state.row.remarks} />
                Customer: <input type="text" value={this.state.row.customer_name} />
            </div>
        );
    }
}

class SalesOrderParentComponent extends React.Component {
    
    render() {
        return (
            <div>
            <SalesOrderTable
                rowClicked={this.rowClicked.bind(this)}
            />
            <SalesOrderEdit ref={(c) => {this.salesOrderEdit = c;}} />
            </div>
        )
    }
    
    rowClicked(r) {
        this.salesOrderEdit.setData(r);
    }
}

if (document.getElementById('sales_order_list')) {
    ReactDOM.render(
        <SalesOrderParentComponent />,
        document.getElementById('sales_order_list'));
}