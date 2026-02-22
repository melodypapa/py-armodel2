"""AtomicSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 304)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 300)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 70)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2000)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 205)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 43)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.symbol_props import (
    SymbolProps,
)
from abc import ABC, abstractmethod


class AtomicSwComponentType(SwComponentType, ABC):
    """AUTOSAR AtomicSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    internal_behavior: Optional[SwcInternalBehavior]
    symbol_props: Optional[SymbolProps]
    def __init__(self) -> None:
        """Initialize AtomicSwComponentType."""
        super().__init__()
        self.internal_behavior: Optional[SwcInternalBehavior] = None
        self.symbol_props: Optional[SymbolProps] = None

    def serialize(self) -> ET.Element:
        """Serialize AtomicSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AtomicSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize internal_behavior
        if self.internal_behavior is not None:
            serialized = SerializationHelper.serialize_item(self.internal_behavior, "SwcInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERNAL-BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize symbol_props
        if self.symbol_props is not None:
            serialized = SerializationHelper.serialize_item(self.symbol_props, "SymbolProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtomicSwComponentType":
        """Deserialize XML element to AtomicSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtomicSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AtomicSwComponentType, cls).deserialize(element)

        # Parse internal_behavior
        child = SerializationHelper.find_child_element(element, "INTERNAL-BEHAVIOR")
        if child is not None:
            internal_behavior_value = SerializationHelper.deserialize_by_tag(child, "SwcInternalBehavior")
            obj.internal_behavior = internal_behavior_value

        # Parse symbol_props
        child = SerializationHelper.find_child_element(element, "SYMBOL-PROPS")
        if child is not None:
            symbol_props_value = SerializationHelper.deserialize_by_tag(child, "SymbolProps")
            obj.symbol_props = symbol_props_value

        return obj



