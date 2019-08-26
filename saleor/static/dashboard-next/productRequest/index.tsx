import * as React from "react";
import { Route, RouteComponentProps, Switch } from "react-router-dom";

import { WindowTitle } from "../components/WindowTitle";
import i18n from "../i18n";
import {ProductRequestUrl,ProductListUrlQueryParams} from './urls'
import ProductRequestPage from './component/ProductRequestPage'

import { parse as parseQs } from "qs";

const ProductRequest: React.StatelessComponent<RouteComponentProps<any>> = ({}) => {
  return <ProductRequestPage />;
};

const ProductRequestCom = () => (
  <>
    <WindowTitle title={i18n.t("ProductRequest")} />
    <Switch>
      <Route exact path={ProductRequestUrl} component={ProductRequest} />
    </Switch>
  </>
);

export default ProductRequestCom;
