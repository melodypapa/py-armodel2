"""EcucChoiceReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 74)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
    EcucAbstractInternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)


class EcucChoiceReferenceDef(EcucAbstractInternalReferenceDef):
    """AUTOSAR EcucChoiceReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize EcucChoiceReferenceDef."""
        super().__init__()
        self.destination_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucChoiceReferenceDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucChoiceReferenceDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_refs (list to container "DESTINATION-REFS")
        if self.destination_refs:
            wrapper = ET.Element("DESTINATION-REFS")
            for item in self.destination_refs:
                serialized = ARObject._serialize_item(item, "EcucContainerDef")
                if serialized is not None:
                    child_elem = ET.Element("DESTINATION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucChoiceReferenceDef":
        """Deserialize XML element to EcucChoiceReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucChoiceReferenceDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucChoiceReferenceDef, cls).deserialize(element)

        # Parse destination_refs (list from container "DESTINATION-REFS")
        obj.destination_refs = []
        container = ARObject._find_child_element(element, "DESTINATION-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.destination_refs.append(child_value)

        return obj



class EcucChoiceReferenceDefBuilder:
    """Builder for EcucChoiceReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucChoiceReferenceDef = EcucChoiceReferenceDef()

    def build(self) -> EcucChoiceReferenceDef:
        """Build and return EcucChoiceReferenceDef object.

        Returns:
            EcucChoiceReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
