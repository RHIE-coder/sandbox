describe("template spec", () => {
  it("passes", () => {
    // cy.visit("https://example.cypress.io");
    cy.visit("http://localhost:5173");
  });

  it("testtest", () => {
    cy.visit("http://localhost:5173");
    cy.get(".card").within(() => {
      cy.get("button").click();
      cy.get("button").click();
      cy.get("button").click();
      cy.get("button").click();
      cy.get("button").click();
      cy.get("button").click();
      cy.get("button").contains("count is 6");
      cy.screenshot();
    });
  });

  after(() => {
    cy.wait(5000);
  });
});
