"""EcucReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 73)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 442)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 189)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
    EcucAbstractInternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)


class EcucReferenceDef(EcucAbstractInternalReferenceDef):
    """AUTOSAR EcucReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination: Optional[EcucContainerDef]
    def __init__(self) -> None:
        """Initialize EcucReferenceDef."""
        super().__init__()
        self.destination: Optional[EcucContainerDef] = None
    def serialize(self) -> ET.Element:
        """Serialize EcucReferenceDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucReferenceDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination
        if self.destination is not None:
            serialized = ARObject._serialize_item(self.destination, "EcucContainerDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucReferenceDef":
        """Deserialize XML element to EcucReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucReferenceDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucReferenceDef, cls).deserialize(element)

        # Parse destination
        child = ARObject._find_child_element(element, "DESTINATION")
        if child is not None:
            destination_value = ARObject._deserialize_by_tag(child, "EcucContainerDef")
            obj.destination = destination_value

        return obj



class EcucReferenceDefBuilder:
    """Builder for EcucReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucReferenceDef = EcucReferenceDef()

    def build(self) -> EcucReferenceDef:
        """Build and return EcucReferenceDef object.

        Returns:
            EcucReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
