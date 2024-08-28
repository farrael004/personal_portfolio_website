import streamlit as st

st.markdown("""# Duplicate Detective""")
st.image("assets/icon.png")
st.markdown(
    """This is a cutting-edge deduplication tool developed using Flet, designed to efficiently identify and manage both exact and near-duplicate files. Built with advanced Computer Vision and Natural Language Processing (NLP) techniques, this tool significantly accelerates the deduplication process, saving over 75% of the time typically required. Originally implemented in AAFC's ATIP, Duplicate Detective proves its efficacy in real-world applications. *(Only distributable upon request)*"""
)
st.image("assets/report.png", width=500)
st.markdown(
    """
    ## Key Features:
    - **Advanced Duplicate Detection:** Duplicate Detective leverages NLP to accurately identify exact and near-duplicate files across various formats. It compares two types of files independently—text files and image files—to ensure thorough and precise detection.

    - **Text and Image Clustering:**

        - **Text Files:** Text content from files is extracted using a combination of Python libraries and Optical Character Recognition (OCR) for files containing images. The extracted text is then vectorized using N-grams and clustered with the DBSCAN algorithm, effectively grouping similar files for easy management.
        - **Image Files:**
            1. Feature Extraction with ORB: We utilized the ORB (Oriented FAST and Rotated BRIEF) algorithm for extracting keypoints and descriptors from images. ORB is a fast, rotation-invariant, and robust feature extractor that identifies unique points in images, facilitating the comparison of different images based on their content.
            2. Image Matching: To determine the similarity between pairs of images, we employed a brute force matcher with the Hamming distance as a metric, optimized to find the best matches for the ORB descriptors. A ratio test filters out less reliable matches, ensuring that only the most similar keypoints contribute to the similarity score.
            3. Clustering with Union-Find: An implementation of the union-find algorithm is used to dynamically cluster images based on their similarity scores. This method efficiently merges images into groups as it iterates through all pairs, identifying connected components within the dataset. The union-find structure is key for minimizing redundant comparisons and accelerating the clustering process.
            4. Homography and RANSAC: For images with a sufficient number of good matches, we calculate a homography matrix using RANSAC (Random Sample Consensus). This step further refines the matching process by considering only geometrically consistent matches, enhancing the accuracy of similarity scores.
            5. Scalable Image Clustering: The end-to-end process, from feature extraction to dynamic clustering, is designed to handle a large number of images. By efficiently comparing images and grouping them based on visual similarity, this package can organize vast datasets into manageable clusters.

    - **Cloud Integration:** The tool seamlessly integrates with popular cloud storage solutions such as Google Cloud, SharePoint Online, OneDrive, and more, enabling users to deduplicate files across multiple platforms without hassle.

    - **Email Attachment Deduplication:** Duplicate Detective is equipped to analyze emails and their attachments, comparing these attachments with other files to identify duplicates. This feature ensures comprehensive deduplication across all file types, including those embedded within emails.

    - **User-Friendly Interface:** Users can easily manage duplicate files through a simple and intuitive interface. The tool displays clustered files in a list, allowing users to open, move, or delete duplicates with just a few clicks.

    - **Multi-Folder Analysis:** Duplicate Detective supports the simultaneous analysis of multiple folders, giving users flexibility in how they approach deduplication tasks. Users can also filter which types of files to analyze, tailoring the process to their specific needs.

    - **Report Generation & Search:** After analysis, users can save detailed reports as PDFs for future reference. The tool also includes a powerful search function, enabling users to search through the text of all scanned files quickly and efficiently.
    """
)
st.image("assets/finished_report.png")
