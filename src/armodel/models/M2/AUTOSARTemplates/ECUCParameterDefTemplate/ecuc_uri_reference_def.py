"""EcucUriReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 81)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
    EcucAbstractInternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)


class EcucUriReferenceDef(EcucAbstractInternalReferenceDef):
    """AUTOSAR EcucUriReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_uri_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize EcucUriReferenceDef."""
        super().__init__()
        self.destination_uri_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucUriReferenceDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucUriReferenceDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_uri_ref
        if self.destination_uri_ref is not None:
            serialized = SerializationHelper.serialize_item(self.destination_uri_ref, "EcucDestinationUriDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-URI-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucUriReferenceDef":
        """Deserialize XML element to EcucUriReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucUriReferenceDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucUriReferenceDef, cls).deserialize(element)

        # Parse destination_uri_ref
        child = SerializationHelper.find_child_element(element, "DESTINATION-URI-REF")
        if child is not None:
            destination_uri_ref_value = ARRef.deserialize(child)
            obj.destination_uri_ref = destination_uri_ref_value

        return obj



class EcucUriReferenceDefBuilder:
    """Builder for EcucUriReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucUriReferenceDef = EcucUriReferenceDef()

    def build(self) -> EcucUriReferenceDef:
        """Build and return EcucUriReferenceDef object.

        Returns:
            EcucUriReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
