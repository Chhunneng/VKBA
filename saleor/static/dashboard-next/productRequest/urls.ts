import { ActiveTab, BulkAction, Dialog, Filters, Pagination } from "../types";
export const ProductRequestUrl = '/productRequest'
export type ProductListUrlDialog =
  | "publish"
  | "unpublish"
  | "delete"
  | "save-search"
  | "delete-search";
  export enum ProductListUrlFiltersEnum {
    isPublished = "isPublished",
    priceFrom = "priceFrom",
    priceTo = "priceTo",
    status = "status",
    query = "query"
  }
export type ProductListUrlFilters = Filters<ProductListUrlFiltersEnum>;
export type ProductListUrlQueryParams = BulkAction &
  Dialog<ProductListUrlDialog> &
  ProductListUrlFilters &
  Pagination &
  ActiveTab;
