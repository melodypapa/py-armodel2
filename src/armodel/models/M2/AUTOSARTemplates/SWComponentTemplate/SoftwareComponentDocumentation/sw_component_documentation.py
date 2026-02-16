"""SwComponentDocumentation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.Chapters.chapter import (
    Chapter,
)


class SwComponentDocumentation(ARObject):
    """AUTOSAR SwComponentDocumentation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("chapters", None, False, True, Chapter),  # chapters
        ("sw_calibration", None, False, False, Chapter),  # swCalibration
        ("sw_carb_doc", None, False, False, Chapter),  # swCarbDoc
        ("sw_diagnostics", None, False, False, Chapter),  # swDiagnostics
        ("sw_feature_def", None, False, False, Chapter),  # swFeatureDef
        ("sw_feature_desc", None, False, False, Chapter),  # swFeatureDesc
        ("sw_maintenance", None, False, False, Chapter),  # swMaintenance
        ("sw_test_desc", None, False, False, Chapter),  # swTestDesc
    ]

    def __init__(self) -> None:
        """Initialize SwComponentDocumentation."""
        super().__init__()
        self.chapters: list[Chapter] = []
        self.sw_calibration: Optional[Chapter] = None
        self.sw_carb_doc: Optional[Chapter] = None
        self.sw_diagnostics: Optional[Chapter] = None
        self.sw_feature_def: Optional[Chapter] = None
        self.sw_feature_desc: Optional[Chapter] = None
        self.sw_maintenance: Optional[Chapter] = None
        self.sw_test_desc: Optional[Chapter] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwComponentDocumentation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentDocumentation":
        """Create SwComponentDocumentation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwComponentDocumentation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwComponentDocumentation since parent returns ARObject
        return cast("SwComponentDocumentation", obj)


class SwComponentDocumentationBuilder:
    """Builder for SwComponentDocumentation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwComponentDocumentation = SwComponentDocumentation()

    def build(self) -> SwComponentDocumentation:
        """Build and return SwComponentDocumentation object.

        Returns:
            SwComponentDocumentation instance
        """
        # TODO: Add validation
        return self._obj
