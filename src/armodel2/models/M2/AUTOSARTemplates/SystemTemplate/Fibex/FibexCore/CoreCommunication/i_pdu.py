"""IPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 341)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 226)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import PduBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.contained_i_pdu_props import (
    ContainedIPduProps,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IPdu(Pdu, ABC):
    """AUTOSAR IPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    contained_i_pdu_props: Optional[ContainedIPduProps]
    _DESERIALIZE_DISPATCH = {
        "CONTAINED-I-PDU-PROPS": lambda obj, elem: setattr(obj, "contained_i_pdu_props", SerializationHelper.deserialize_by_tag(elem, "ContainedIPduProps")),
    }


    def __init__(self) -> None:
        """Initialize IPdu."""
        super().__init__()
        self.contained_i_pdu_props: Optional[ContainedIPduProps] = None

    def serialize(self) -> ET.Element:
        """Serialize IPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize contained_i_pdu_props
        if self.contained_i_pdu_props is not None:
            serialized = SerializationHelper.serialize_item(self.contained_i_pdu_props, "ContainedIPduProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTAINED-I-PDU-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPdu":
        """Deserialize XML element to IPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPdu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTAINED-I-PDU-PROPS":
                setattr(obj, "contained_i_pdu_props", SerializationHelper.deserialize_by_tag(child, "ContainedIPduProps"))

        return obj



class IPduBuilder(PduBuilder):
    """Builder for IPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IPdu = IPdu()


    def with_contained_i_pdu_props(self, value: Optional[ContainedIPduProps]) -> "IPduBuilder":
        """Set contained_i_pdu_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'contained_i_pdu_props' is required and cannot be None")
        self._obj.contained_i_pdu_props = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "containedIPduProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> IPdu:
        """Build and return the IPdu instance (abstract)."""
        raise NotImplementedError