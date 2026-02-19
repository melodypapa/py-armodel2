"""SwComponentDocumentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 337)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 697)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 465)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SoftwareComponentDocumentation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.Chapters.chapter import (
    Chapter,
)


class SwComponentDocumentation(ARObject):
    """AUTOSAR SwComponentDocumentation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    chapters: list[Chapter]
    sw_calibration: Optional[Chapter]
    sw_carb_doc: Optional[Chapter]
    sw_diagnostics: Optional[Chapter]
    sw_feature_def: Optional[Chapter]
    sw_feature_desc: Optional[Chapter]
    sw_maintenance: Optional[Chapter]
    sw_test_desc: Optional[Chapter]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentDocumentation":
        """Deserialize XML element to SwComponentDocumentation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwComponentDocumentation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse chapters (list)
        obj.chapters = []
        for child in ARObject._find_all_child_elements(element, "CHAPTERS"):
            chapters_value = ARObject._deserialize_by_tag(child, "Chapter")
            obj.chapters.append(chapters_value)

        # Parse sw_calibration
        child = ARObject._find_child_element(element, "SW-CALIBRATION")
        if child is not None:
            sw_calibration_value = ARObject._deserialize_by_tag(child, "Chapter")
            obj.sw_calibration = sw_calibration_value

        # Parse sw_carb_doc
        child = ARObject._find_child_element(element, "SW-CARB-DOC")
        if child is not None:
            sw_carb_doc_value = ARObject._deserialize_by_tag(child, "Chapter")
            obj.sw_carb_doc = sw_carb_doc_value

        # Parse sw_diagnostics
        child = ARObject._find_child_element(element, "SW-DIAGNOSTICS")
        if child is not None:
            sw_diagnostics_value = ARObject._deserialize_by_tag(child, "Chapter")
            obj.sw_diagnostics = sw_diagnostics_value

        # Parse sw_feature_def
        child = ARObject._find_child_element(element, "SW-FEATURE-DEF")
        if child is not None:
            sw_feature_def_value = ARObject._deserialize_by_tag(child, "Chapter")
            obj.sw_feature_def = sw_feature_def_value

        # Parse sw_feature_desc
        child = ARObject._find_child_element(element, "SW-FEATURE-DESC")
        if child is not None:
            sw_feature_desc_value = ARObject._deserialize_by_tag(child, "Chapter")
            obj.sw_feature_desc = sw_feature_desc_value

        # Parse sw_maintenance
        child = ARObject._find_child_element(element, "SW-MAINTENANCE")
        if child is not None:
            sw_maintenance_value = ARObject._deserialize_by_tag(child, "Chapter")
            obj.sw_maintenance = sw_maintenance_value

        # Parse sw_test_desc
        child = ARObject._find_child_element(element, "SW-TEST-DESC")
        if child is not None:
            sw_test_desc_value = ARObject._deserialize_by_tag(child, "Chapter")
            obj.sw_test_desc = sw_test_desc_value

        return obj



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
