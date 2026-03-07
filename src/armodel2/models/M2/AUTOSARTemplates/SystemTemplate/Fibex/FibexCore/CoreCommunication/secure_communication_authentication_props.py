"""SecureCommunicationAuthenticationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 371)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecureCommunicationAuthenticationProps(Identifiable):
    """AUTOSAR SecureCommunicationAuthenticationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURE-COMMUNICATION-AUTHENTICATION-PROPS"


    auth_info_tx: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "AUTH-INFO-TX": lambda obj, elem: setattr(obj, "auth_info_tx", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize SecureCommunicationAuthenticationProps."""
        super().__init__()
        self.auth_info_tx: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SecureCommunicationAuthenticationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecureCommunicationAuthenticationProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize auth_info_tx
        if self.auth_info_tx is not None:
            serialized = SerializationHelper.serialize_item(self.auth_info_tx, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTH-INFO-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationAuthenticationProps":
        """Deserialize XML element to SecureCommunicationAuthenticationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecureCommunicationAuthenticationProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecureCommunicationAuthenticationProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AUTH-INFO-TX":
                setattr(obj, "auth_info_tx", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class SecureCommunicationAuthenticationPropsBuilder(IdentifiableBuilder):
    """Builder for SecureCommunicationAuthenticationProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecureCommunicationAuthenticationProps = SecureCommunicationAuthenticationProps()


    def with_auth_info_tx(self, value: Optional[PositiveInteger]) -> "SecureCommunicationAuthenticationPropsBuilder":
        """Set auth_info_tx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'auth_info_tx' is required and cannot be None")
        self._obj.auth_info_tx = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "authInfoTx",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SecureCommunicationAuthenticationProps:
        """Build and return the SecureCommunicationAuthenticationProps instance with validation."""
        self._validate_instance()
        return self._obj