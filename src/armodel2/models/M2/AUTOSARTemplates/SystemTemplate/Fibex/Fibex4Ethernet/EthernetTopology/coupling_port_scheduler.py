"""CouplingPortScheduler AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 123)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import CouplingPortStructuralElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetCouplingPortSchedulerEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CouplingPortScheduler(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortScheduler."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COUPLING-PORT-SCHEDULER"


    port_scheduler_scheduler_enum: Optional[EthernetCouplingPortSchedulerEnum]
    predecessor_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PORT-SCHEDULER-SCHEDULER-ENUM": lambda obj, elem: setattr(obj, "port_scheduler_scheduler_enum", EthernetCouplingPortSchedulerEnum.deserialize(elem)),
        "PREDECESSOR-REFS": ("_POLYMORPHIC_LIST", "predecessor_refs", ["CouplingPortFifo", "CouplingPortScheduler", "CouplingPortShaper"]),
    }


    def __init__(self) -> None:
        """Initialize CouplingPortScheduler."""
        super().__init__()
        self.port_scheduler_scheduler_enum: Optional[EthernetCouplingPortSchedulerEnum] = None
        self.predecessor_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize CouplingPortScheduler to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortScheduler, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize port_scheduler_scheduler_enum
        if self.port_scheduler_scheduler_enum is not None:
            serialized = SerializationHelper.serialize_item(self.port_scheduler_scheduler_enum, "EthernetCouplingPortSchedulerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-SCHEDULER-SCHEDULER-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize predecessor_refs (list to container "PREDECESSOR-REFS")
        if self.predecessor_refs:
            wrapper = ET.Element("PREDECESSOR-REFS")
            for item in self.predecessor_refs:
                serialized = SerializationHelper.serialize_item(item, "CouplingPortStructuralElement")
                if serialized is not None:
                    child_elem = ET.Element("PREDECESSOR-REF")
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
    def deserialize(cls, element: ET.Element) -> "CouplingPortScheduler":
        """Deserialize XML element to CouplingPortScheduler object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortScheduler object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortScheduler, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PORT-SCHEDULER-SCHEDULER-ENUM":
                setattr(obj, "port_scheduler_scheduler_enum", EthernetCouplingPortSchedulerEnum.deserialize(child))
            elif tag == "PREDECESSOR-REFS":
                for item_elem in child:
                    obj.predecessor_refs.append(ARRef.deserialize(item_elem))

        return obj



class CouplingPortSchedulerBuilder(CouplingPortStructuralElementBuilder):
    """Builder for CouplingPortScheduler with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CouplingPortScheduler = CouplingPortScheduler()


    def with_port_scheduler_scheduler_enum(self, value: Optional[EthernetCouplingPortSchedulerEnum]) -> "CouplingPortSchedulerBuilder":
        """Set port_scheduler_scheduler_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.port_scheduler_scheduler_enum = value
        return self

    def with_predecessors(self, items: list[CouplingPortStructuralElement]) -> "CouplingPortSchedulerBuilder":
        """Set predecessors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.predecessors = list(items) if items else []
        return self


    def add_predecessor(self, item: CouplingPortStructuralElement) -> "CouplingPortSchedulerBuilder":
        """Add a single item to predecessors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.predecessors.append(item)
        return self

    def clear_predecessors(self) -> "CouplingPortSchedulerBuilder":
        """Clear all items from predecessors list.

        Returns:
            self for method chaining
        """
        self._obj.predecessors = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "portSchedulerSchedulerEnum",
        "predecessor",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CouplingPortScheduler:
        """Build and return the CouplingPortScheduler instance with validation."""
        self._validate_instance()
        return self._obj