<html>
<?php
$filename=basename(__FILE__, '.php').".rss";
?>
<body>
    <h1 style="text-align:center;margin-bottom:0">
        Meeting Notes
        <a href="<?php echo $filename; ?>"><img src="https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Feed-icon.svg/16px-Feed-icon.svg.png"></a>
    </h1>

    <?php
    include_once("rss2html.php");
    output_rss_feed($filename);
    ?>
</body>
