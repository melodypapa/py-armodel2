"""GeneralPurposeIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 345)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 60)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class GeneralPurposeIPdu(IPdu):
    """AUTOSAR GeneralPurposeIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize GeneralPurposeIPdu."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize GeneralPurposeIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GeneralPurposeIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GeneralPurposeIPdu":
        """Deserialize XML element to GeneralPurposeIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GeneralPurposeIPdu object
        """
        # Delegate to parent class to handle inherited attributes
        return super(GeneralPurposeIPdu, cls).deserialize(element)



class GeneralPurposeIPduBuilder:
    """Builder for GeneralPurposeIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GeneralPurposeIPdu = GeneralPurposeIPdu()

    def build(self) -> GeneralPurposeIPdu:
        """Build and return GeneralPurposeIPdu object.

        Returns:
            GeneralPurposeIPdu instance
        """
        # TODO: Add validation
        return self._obj
