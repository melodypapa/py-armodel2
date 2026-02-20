"""ClientServerAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 155)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientServerAnnotation(GeneralAnnotation):
    """AUTOSAR ClientServerAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ClientServerAnnotation."""
        super().__init__()
        self.operation_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ClientServerAnnotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerAnnotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operation_ref
        if self.operation_ref is not None:
            serialized = ARObject._serialize_item(self.operation_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerAnnotation":
        """Deserialize XML element to ClientServerAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerAnnotation, cls).deserialize(element)

        # Parse operation_ref
        child = ARObject._find_child_element(element, "OPERATION-REF")
        if child is not None:
            operation_ref_value = ARRef.deserialize(child)
            obj.operation_ref = operation_ref_value

        return obj



class ClientServerAnnotationBuilder:
    """Builder for ClientServerAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerAnnotation = ClientServerAnnotation()

    def build(self) -> ClientServerAnnotation:
        """Build and return ClientServerAnnotation object.

        Returns:
            ClientServerAnnotation instance
        """
        # TODO: Add validation
        return self._obj
