"""SubElementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SubElementMapping(ARObject):
    """AUTOSAR SubElementMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_element_ref: Optional[ARRef]
    second_element_ref: Optional[ARRef]
    text_table_ref: ARRef
    def __init__(self) -> None:
        """Initialize SubElementMapping."""
        super().__init__()
        self.first_element_ref: Optional[ARRef] = None
        self.second_element_ref: Optional[ARRef] = None
        self.text_table_ref: ARRef = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SubElementMapping":
        """Deserialize XML element to SubElementMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SubElementMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse first_element_ref
        child = ARObject._find_child_element(element, "FIRST-ELEMENT")
        if child is not None:
            first_element_ref_value = ARObject._deserialize_by_tag(child, "SubElementRef")
            obj.first_element_ref = first_element_ref_value

        # Parse second_element_ref
        child = ARObject._find_child_element(element, "SECOND-ELEMENT")
        if child is not None:
            second_element_ref_value = ARObject._deserialize_by_tag(child, "SubElementRef")
            obj.second_element_ref = second_element_ref_value

        # Parse text_table_ref
        child = ARObject._find_child_element(element, "TEXT-TABLE")
        if child is not None:
            text_table_ref_value = ARObject._deserialize_by_tag(child, "TextTableMapping")
            obj.text_table_ref = text_table_ref_value

        return obj



class SubElementMappingBuilder:
    """Builder for SubElementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SubElementMapping = SubElementMapping()

    def build(self) -> SubElementMapping:
        """Build and return SubElementMapping object.

        Returns:
            SubElementMapping instance
        """
        # TODO: Add validation
        return self._obj
