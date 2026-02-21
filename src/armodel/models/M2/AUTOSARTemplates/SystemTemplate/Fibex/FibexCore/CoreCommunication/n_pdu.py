"""NPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 301)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 343)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class NPdu(IPdu):
    """AUTOSAR NPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize NPdu."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize NPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NPdu":
        """Deserialize XML element to NPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NPdu object
        """
        # Delegate to parent class to handle inherited attributes
        return super(NPdu, cls).deserialize(element)



class NPduBuilder:
    """Builder for NPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NPdu = NPdu()

    def build(self) -> NPdu:
        """Build and return NPdu object.

        Returns:
            NPdu instance
        """
        # TODO: Add validation
        return self._obj
