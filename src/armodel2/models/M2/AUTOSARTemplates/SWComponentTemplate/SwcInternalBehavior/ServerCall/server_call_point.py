"""ServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 335)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 580)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2055)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServerCall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import AbstractAccessPointBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.r_operation_in_atomic_swc_instance_ref import (
        ROperationInAtomicSwcInstanceRef,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ServerCallPoint(AbstractAccessPoint, ABC):
    """AUTOSAR ServerCallPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    operation_iref: Optional[ROperationInAtomicSwcInstanceRef]
    timeout: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "OPERATION-IREF": lambda obj, elem: setattr(obj, "operation_iref", SerializationHelper.deserialize_by_tag(elem, "ROperationInAtomicSwcInstanceRef")),
        "TIMEOUT": lambda obj, elem: setattr(obj, "timeout", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize ServerCallPoint."""
        super().__init__()
        self.operation_iref: Optional[ROperationInAtomicSwcInstanceRef] = None
        self.timeout: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize ServerCallPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ServerCallPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operation_iref (instance reference with wrapper "OPERATION-IREF")
        if self.operation_iref is not None:
            serialized = SerializationHelper.serialize_item(self.operation_iref, "ROperationInAtomicSwcInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("OPERATION-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        # Serialize timeout
        if self.timeout is not None:
            serialized = SerializationHelper.serialize_item(self.timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServerCallPoint":
        """Deserialize XML element to ServerCallPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ServerCallPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ServerCallPoint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OPERATION-IREF":
                setattr(obj, "operation_iref", SerializationHelper.deserialize_by_tag(child, "ROperationInAtomicSwcInstanceRef"))
            elif tag == "TIMEOUT":
                setattr(obj, "timeout", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class ServerCallPointBuilder(AbstractAccessPointBuilder):
    """Builder for ServerCallPoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ServerCallPoint = ServerCallPoint()


    def with_operation(self, value: Optional[ROperationInAtomicSwcInstanceRef]) -> "ServerCallPointBuilder":
        """Set operation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'operation' is required and cannot be None")
        self._obj.operation = value
        return self

    def with_timeout(self, value: Optional[TimeValue]) -> "ServerCallPointBuilder":
        """Set timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'timeout' is required and cannot be None")
        self._obj.timeout = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "operation",
        "timeout",
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
    def build(self) -> ServerCallPoint:
        """Build and return the ServerCallPoint instance (abstract)."""
        raise NotImplementedError