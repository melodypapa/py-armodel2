"""BlockState AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BlockState(Identifiable):
    """AUTOSAR BlockState."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize BlockState."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize BlockState to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BlockState, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlockState":
        """Deserialize XML element to BlockState object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlockState object
        """
        # Delegate to parent class to handle inherited attributes
        return super(BlockState, cls).deserialize(element)



class BlockStateBuilder:
    """Builder for BlockState."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlockState = BlockState()

    def build(self) -> BlockState:
        """Build and return BlockState object.

        Returns:
            BlockState instance
        """
        # TODO: Add validation
        return self._obj
