import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import {
  createStyles,
  Theme,
  withStyles,
  WithStyles
} from "@material-ui/core/styles";
import * as React from "react";

import CardTitle from "@saleor/components/CardTitle";
import FormSpacer from "@saleor/components/FormSpacer";
import i18n from "../../../i18n";

const styles = (theme: Theme) =>
  createStyles({
    root: {
      display: "grid",
      gridColumnGap: theme.spacing.unit * 2 + "px",
      gridTemplateColumns: `3fr 1fr`
    }
  });

interface ProductRequestPageProps extends WithStyles<typeof styles> {
}

export const ProductRequestPage = withStyles(styles, {
  name: "ProductRequest"
})(
  ({
    classes
  }: ProductRequestPageProps) => (
    <Card>
      <CardTitle title={i18n.t("Product Request")} />
      <CardContent>
        <div className={classes.root}>
          Hello Chhunnneng
        </div>
        <FormSpacer />
      </CardContent>
    </Card>
  )
);
ProductRequestPage.displayName = "ProductRequestPage";
export default ProductRequestPage;
