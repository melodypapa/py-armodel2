"""SecuredIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 367)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    SecuredPduHeaderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class SecuredIPdu(IPdu):
    """AUTOSAR SecuredIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication_ref: Optional[Any]
    dynamic: Optional[Boolean]
    freshness_props_ref: Optional[Any]
    payload_ref: Optional[ARRef]
    secure: Optional[Any]
    use_as: Optional[Boolean]
    use_secured_pdu: Optional[SecuredPduHeaderEnum]
    def __init__(self) -> None:
        """Initialize SecuredIPdu."""
        super().__init__()
        self.authentication_ref: Optional[Any] = None
        self.dynamic: Optional[Boolean] = None
        self.freshness_props_ref: Optional[Any] = None
        self.payload_ref: Optional[ARRef] = None
        self.secure: Optional[Any] = None
        self.use_as: Optional[Boolean] = None
        self.use_secured_pdu: Optional[SecuredPduHeaderEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize SecuredIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecuredIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentication_ref
        if self.authentication_ref is not None:
            serialized = ARObject._serialize_item(self.authentication_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTHENTICATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dynamic
        if self.dynamic is not None:
            serialized = ARObject._serialize_item(self.dynamic, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize freshness_props_ref
        if self.freshness_props_ref is not None:
            serialized = ARObject._serialize_item(self.freshness_props_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRESHNESS-PROPS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize payload_ref
        if self.payload_ref is not None:
            serialized = ARObject._serialize_item(self.payload_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PAYLOAD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize secure
        if self.secure is not None:
            serialized = ARObject._serialize_item(self.secure, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_as
        if self.use_as is not None:
            serialized = ARObject._serialize_item(self.use_as, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-AS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_secured_pdu
        if self.use_secured_pdu is not None:
            serialized = ARObject._serialize_item(self.use_secured_pdu, "SecuredPduHeaderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-SECURED-PDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecuredIPdu":
        """Deserialize XML element to SecuredIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecuredIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecuredIPdu, cls).deserialize(element)

        # Parse authentication_ref
        child = ARObject._find_child_element(element, "AUTHENTICATION-REF")
        if child is not None:
            authentication_ref_value = ARRef.deserialize(child)
            obj.authentication_ref = authentication_ref_value

        # Parse dynamic
        child = ARObject._find_child_element(element, "DYNAMIC")
        if child is not None:
            dynamic_value = child.text
            obj.dynamic = dynamic_value

        # Parse freshness_props_ref
        child = ARObject._find_child_element(element, "FRESHNESS-PROPS-REF")
        if child is not None:
            freshness_props_ref_value = ARRef.deserialize(child)
            obj.freshness_props_ref = freshness_props_ref_value

        # Parse payload_ref
        child = ARObject._find_child_element(element, "PAYLOAD-REF")
        if child is not None:
            payload_ref_value = ARRef.deserialize(child)
            obj.payload_ref = payload_ref_value

        # Parse secure
        child = ARObject._find_child_element(element, "SECURE")
        if child is not None:
            secure_value = child.text
            obj.secure = secure_value

        # Parse use_as
        child = ARObject._find_child_element(element, "USE-AS")
        if child is not None:
            use_as_value = child.text
            obj.use_as = use_as_value

        # Parse use_secured_pdu
        child = ARObject._find_child_element(element, "USE-SECURED-PDU")
        if child is not None:
            use_secured_pdu_value = SecuredPduHeaderEnum.deserialize(child)
            obj.use_secured_pdu = use_secured_pdu_value

        return obj



class SecuredIPduBuilder:
    """Builder for SecuredIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecuredIPdu = SecuredIPdu()

    def build(self) -> SecuredIPdu:
        """Build and return SecuredIPdu object.

        Returns:
            SecuredIPdu instance
        """
        # TODO: Add validation
        return self._obj
