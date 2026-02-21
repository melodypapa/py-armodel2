"""EcucDestinationUriDefSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)


class EcucDestinationUriDefSet(ARElement):
    """AUTOSAR EcucDestinationUriDefSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_uri_defs: list[EcucDestinationUriDef]
    def __init__(self) -> None:
        """Initialize EcucDestinationUriDefSet."""
        super().__init__()
        self.destination_uri_defs: list[EcucDestinationUriDef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucDestinationUriDefSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucDestinationUriDefSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_uri_defs (list to container "DESTINATION-URI-DEFS")
        if self.destination_uri_defs:
            wrapper = ET.Element("DESTINATION-URI-DEFS")
            for item in self.destination_uri_defs:
                serialized = ARObject._serialize_item(item, "EcucDestinationUriDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriDefSet":
        """Deserialize XML element to EcucDestinationUriDefSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDestinationUriDefSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucDestinationUriDefSet, cls).deserialize(element)

        # Parse destination_uri_defs (list from container "DESTINATION-URI-DEFS")
        obj.destination_uri_defs = []
        container = ARObject._find_child_element(element, "DESTINATION-URI-DEFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.destination_uri_defs.append(child_value)

        return obj



class EcucDestinationUriDefSetBuilder:
    """Builder for EcucDestinationUriDefSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriDefSet = EcucDestinationUriDefSet()

    def build(self) -> EcucDestinationUriDefSet:
        """Build and return EcucDestinationUriDefSet object.

        Returns:
            EcucDestinationUriDefSet instance
        """
        # TODO: Add validation
        return self._obj
