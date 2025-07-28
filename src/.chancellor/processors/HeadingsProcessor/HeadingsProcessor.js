async function process(source, metadata) {
    const { frontMatter, projectVariables } = metadata;

    // Find all HTML headings (h1 to h6) in the source
    const regex = /<h[1-6][^>]*>(.*?)<\/h[1-6]>/gi;
    
    let contentBeforeFirstHeading = /^(\s.*?)<h[1-6][^>]*>/s.test(source.trim());
    let firstHeadingProcessed = false;
    
    // Replace only the first heading if there's prior content, and all subsequent ones
    source = source.replace(regex, (match) => {
        if (!firstHeadingProcessed) {
            firstHeadingProcessed = true;
            return contentBeforeFirstHeading ? `<br><br>${match}` : match;
        }
        return `<br><br>${match}`;
    });

    return source;
}

module.exports = {
    name: "HeadingsProcessor",
    process
};
