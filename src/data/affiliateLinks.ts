// src/data/affiliateLinks.ts
// Central affiliate link registry for New England Crust
// Tag: newenglandcru-20
//
// Each product has:
//   id         — slug used in <AffiliateLink id="..." /> calls in .md posts
//   name       — display name rendered as link text
//   short      — amzn.to short URL (preferred for cleanliness)
//   full       — full tagged URL (fallback / canonical)
//   category   — used for grouping on a gear/links page

export interface AffiliateProduct {
  id: string;
  name: string;
  short: string;
  full: string;
  category: "oven" | "cover" | "peel" | "stand" | "thermometer" | "pellets" | "cord" | "griddle" | "ingredient" | "tool";
}

export const affiliateLinks: AffiliateProduct[] = [
  {
    id: "ninja-woodfire-oven",
    name: "Ninja Woodfire 8-in-1 Outdoor Oven (OO101)",
    short: "https://amzn.to/4obF5K3",
    full: "https://www.amazon.com/Ninja-Woodfire-Technology-terracotta-OO101/dp/B0C6BQVDX3?linkCode=ll2&tag=newenglandcru-20&linkId=45b84d17b9f75a52a044df93d553e236",
    category: "oven",
  },
  {
    id: "ninja-cover",
    name: "Ninja XSKOCVR Premium Cover",
    short: "https://amzn.to/4vpQc4D",
    full: "https://www.amazon.com/Ninja-XSKOCVR-Drawstrings-Water-Resistant-Lightweight/dp/B0C7LJ76BT?linkCode=ll2&tag=newenglandcru-20&linkId=5048012a3f36c5db8e127f06d7eeb05e",
    category: "cover",
  },
  {
    id: "third-party-cover",
    name: "TRAVELIT Heavy-Duty Oven Cover (OO100 series)",
    short: "https://amzn.to/4o2c4k0",
    full: "https://www.amazon.com/TRAVELIT-Waterproof-Adjustable-Drawstrings-Accessories/dp/B0CFV6GN9K?linkCode=ll2&tag=newenglandcru-20&linkId=65b002b44187d71cd9016b221efc89c9",
    category: "cover",
  },
  {
    id: "ninja-peel",
    name: "Ninja XSKOPPL Perforated Pizza Peel",
    short: "https://amzn.to/3PVphhJ",
    full: "https://www.amazon.com/Ninja-XSKOPPL-Perforated-Compatible-Drawstring/dp/B0C7LH4K38?linkCode=ll2&tag=newenglandcru-20&linkId=4f9547bbe4a1f523f4746a2dd1df6f66",
    category: "peel",
  },
  {
    id: "generic-peel",
    name: "TKC 12-Inch Perforated Aluminum Pizza Peel",
    short: "https://amzn.to/4dRGlgB",
    full: "https://www.amazon.com/TKC-Pizza-Peel-inch-Perforated/dp/B08VTTTMM9?linkCode=ll2&tag=newenglandcru-20&linkId=a9ec6cb4843264489c46dadf2ccbe2be",
    category: "peel",
  },
  {
    id: "ninja-stand",
    name: "Ninja XSKSTAND Collapsible Outdoor Stand",
    short: "https://amzn.to/4veDoOm",
    full: "https://www.amazon.com/Ninja-XSKSTAND-Collapsible-Compatible-Weather-Resistant/dp/B0B9T8FXK1?linkCode=ll2&tag=newenglandcru-20&linkId=496ff08754680c7f4a89992b1b03ff1b",
    category: "stand",
  },
  {
    id: "keter-stand",
    name: "Keter Unity XL Outdoor Storage & Entertainment Station",
    short: "https://amzn.to/3PxJNFi",
    full: "https://www.amazon.com/Keter-Outdoor-Entertainment-Storage-Station/dp/B01HJATSC4?linkCode=ll2&tag=newenglandcru-20&linkId=cdeb8c7899b8fa8bc6814d5ccc0087d8",
    category: "stand",
  },
  {
    id: "infrared-thermometer",
    name: "Etekcity Infrared Thermometer",
    short: "https://amzn.to/3RHkZLA",
    full: "https://www.amazon.com/Etekcity-Infrared-Thermometer-Temperature-Adjustable/dp/B0BGX95FF4?linkCode=ll2&tag=newenglandcru-20&linkId=baabe3e1a1920c982dda698d4d5d9448",
    category: "thermometer",
  },
  {
    id: "robust-blend-pellets",
    name: "Ninja Woodfire Robust Blend Pellets",
    short: "https://amzn.to/3RK2I06",
    full: "https://www.amazon.com/Ninja-XSKOP2R-Woodfire-Sessions-Compatible/dp/B0BBH97TKK?linkCode=ll2&tag=newenglandcru-20&linkId=b5f56ef8abcb844eb9d559ae1cbc316c",
    category: "pellets",
  },
  {
    id: "all-purpose-pellets",
    name: "Ninja Woodfire All-Purpose Blend Pellets",
    short: "https://amzn.to/4uLFVzK",
    full: "https://www.amazon.com/Ninja-Woodfire-Pellets-Compatible-XSKOP5AP/dp/B0FLFGQJTG?linkCode=ll2&tag=newenglandcru-20&linkId=174ac7841f94e83ee207ecf502daef3a",
    category: "pellets",
  },
  {
    id: "kona-pellets",
    name: "Kona Wood Pellets Variety Pack",
    short: "https://amzn.to/4dXNZGe",
    full: "https://www.amazon.com/Kona-Pellets-Intended-Woodfire-Resealable/dp/B0BGJGN8VW?linkCode=ll2&tag=newenglandcru-20&linkId=7e4c28d105df36df0d5d84ec807c312d",
    category: "pellets",
  },
  {
    id: "extension-cord",
    name: "12-Gauge 25-Foot Outdoor Extension Cord",
    short: "https://amzn.to/4wX0Pxb",
    full: "https://www.amazon.com/Outdoor-Extension-3-Outlets-Waterproof-Lighted/dp/B0B8Z6YHPD?linkCode=ll2&tag=newenglandcru-20&linkId=9bb740115bdf96510140db6805961f0b",
    category: "cord",
  },
  {
    id: "outspark-griddle",
    name: "Outspark Porcelain Steel Griddle Pan (OO101 compatible)",
    short: "https://amzn.to/3QcD1VC",
    full: "https://www.amazon.com/Outspark-Porcelain-Woodfire-Non-Stick-Accessories/dp/B0FYG586X4?linkCode=ll2&tag=newenglandcru-20&linkId=a492bb89c1ef4ffecc7a21252533368c",
    category: "griddle",
  },
  {
    id: "caputo-flour",
    name: "Antimo Caputo 00 Pizzeria Flour",
    short: "https://amzn.to/49zTLwF",
    full: "https://www.amazon.com/Antimo-Caputo-Pizzeria-Flour-Blue/dp/B08KB4488S?linkCode=ll2&tag=newenglandcru-20&linkId=935e9486fd66180f9298b5af654c4375",
    category: "ingredient",
  },
  {
    id: "caputo-yeast",
    name: "Caputo Dry Yeast",
    short: "https://amzn.to/4uR6CmM",
    full: "https://www.amazon.com/Dry-Yeast-100-Italian-Mulino/dp/B083FXYGM9?linkCode=ll2&tag=newenglandcru-20&linkId=699fbbee54b590b0aa57965e068da1a0",
    category: "ingredient",
  },
  {
    id: "baleine-sea-salt",
    name: "Baleine Fine Sea Salt",
    short: "https://amzn.to/4fZukIy",
    full: "https://www.amazon.com/Baleine-Salt-Crystals-Canister-Ounce/dp/B000VHNOSM?linkCode=ll2&tag=newenglandcru-20&linkId=3c3705cc42ae1e26d52cc5f298b3e93b",
    category: "ingredient",
  },
  {
    id: "cuisinart-3in1-oven",
    name: "Cuisinart CGG-403 3-in-1 Pizza Oven, Griddle & Grill",
    short: "https://amzn.to/43DuWwe",
    full: "https://www.amazon.com/Cuisinart-CGG-403-Pizza-Griddle-Grill/dp/B09MYF3BXW?linkCode=ll2&tag=newenglandcru-20&linkId=a53387261f58ec13f3d60c3831d56fda",
    category: "oven",
  },
  {
    id: "cuisinart-bread-maker",
    name: "Cuisinart CBK-110 Compact Bread Maker",
    short: "https://amzn.to/4uTS3P9",
    full: "https://www.amazon.com/Cuisinart-CBK-110-Compact-Automatic-Silver/dp/B07C8V4FDR?linkCode=ll2&tag=newenglandcru-20&linkId=362e9b00cf934c18288316910a6455a1",
    category: "tool",
  },
  {
    id: "oxo-bench-scraper",
    name: "OXO Good Grips Bench Scraper",
    short: "https://amzn.to/43ZCHwC",
    full: "https://amzn.to/43ZCHwC",
    category: "tool",
  },
  {
    id: "etekcity-scale",
    name: "Etekcity Digital Kitchen Scale",
    short: "https://amzn.to/4dVhJ84",
    full: "https://amzn.to/4dVhJ84",
    category: "tool",
  },
  {
    id: "gorilla-grip-mitts",
    name: "Gorilla Grip Silicone Oven Mitts",
    short: "https://amzn.to/4fB2SAS",
    full: "https://amzn.to/4fB2SAS",
    category: "tool",
  },
  {
    id: "chef-pomodoro-proofing-box",
    name: "Chef Pomodoro Pizza Dough Proofing Box",
    short: "https://amzn.to/4oBSStP",
    full: "https://amzn.to/4oBSStP",
    category: "tool",
  },
];

// Helper: get a single product by id
export function getLink(id: string): AffiliateProduct | undefined {
  return affiliateLinks.find((p) => p.id === id);
}
