"""TargetIPduRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 841)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.pdu_mapping_default_value import (
    PduMappingDefaultValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class TargetIPduRef(ARObject):
    """AUTOSAR TargetIPduRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_value_ref: Optional[ARRef]
    target_i_pdu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TargetIPduRef."""
        super().__init__()
        self.default_value_ref: Optional[ARRef] = None
        self.target_i_pdu_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize TargetIPduRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize default_value_ref
        if self.default_value_ref is not None:
            serialized = ARObject._serialize_item(self.default_value_ref, "PduMappingDefaultValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_i_pdu_ref
        if self.target_i_pdu_ref is not None:
            serialized = ARObject._serialize_item(self.target_i_pdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-I-PDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TargetIPduRef":
        """Deserialize XML element to TargetIPduRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TargetIPduRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse default_value_ref
        child = ARObject._find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_ref_value = ARObject._deserialize_by_tag(child, "PduMappingDefaultValue")
            obj.default_value_ref = default_value_ref_value

        # Parse target_i_pdu_ref
        child = ARObject._find_child_element(element, "TARGET-I-PDU")
        if child is not None:
            target_i_pdu_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.target_i_pdu_ref = target_i_pdu_ref_value

        return obj



class TargetIPduRefBuilder:
    """Builder for TargetIPduRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TargetIPduRef = TargetIPduRef()

    def build(self) -> TargetIPduRef:
        """Build and return TargetIPduRef object.

        Returns:
            TargetIPduRef instance
        """
        # TODO: Add validation
        return self._obj
