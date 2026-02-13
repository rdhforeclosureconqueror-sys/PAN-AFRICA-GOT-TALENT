export type MemberSnapshot = {
  stars: number;
  blackDollars: number;
  tier: string;
};

export const demoState: MemberSnapshot = {
  stars: 12,
  blackDollars: 55,
  tier: 'Top 25%'
};
