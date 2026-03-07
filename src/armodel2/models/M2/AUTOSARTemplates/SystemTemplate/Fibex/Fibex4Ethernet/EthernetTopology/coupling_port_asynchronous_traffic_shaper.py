"""CouplingPortAsynchronousTrafficShaper AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2012)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_asynchronous_traffic_shaper_group_entry import (
    SwitchAsynchronousTrafficShaperGroupEntry,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CouplingPortAsynchronousTrafficShaper(Identifiable):
    """AUTOSAR CouplingPortAsynchronousTrafficShaper."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER"


    committed_burst: Optional[PositiveInteger]
    committed: Optional[PositiveInteger]
    traffic_shaper_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COMMITTED-BURST": lambda obj, elem: setattr(obj, "committed_burst", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "COMMITTED": lambda obj, elem: setattr(obj, "committed", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TRAFFIC-SHAPER-REF": lambda obj, elem: setattr(obj, "traffic_shaper_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CouplingPortAsynchronousTrafficShaper."""
        super().__init__()
        self.committed_burst: Optional[PositiveInteger] = None
        self.committed: Optional[PositiveInteger] = None
        self.traffic_shaper_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CouplingPortAsynchronousTrafficShaper to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortAsynchronousTrafficShaper, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize committed_burst
        if self.committed_burst is not None:
            serialized = SerializationHelper.serialize_item(self.committed_burst, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMITTED-BURST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize committed
        if self.committed is not None:
            serialized = SerializationHelper.serialize_item(self.committed, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMITTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize traffic_shaper_ref
        if self.traffic_shaper_ref is not None:
            serialized = SerializationHelper.serialize_item(self.traffic_shaper_ref, "SwitchAsynchronousTrafficShaperGroupEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRAFFIC-SHAPER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortAsynchronousTrafficShaper":
        """Deserialize XML element to CouplingPortAsynchronousTrafficShaper object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortAsynchronousTrafficShaper object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortAsynchronousTrafficShaper, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMMITTED-BURST":
                setattr(obj, "committed_burst", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "COMMITTED":
                setattr(obj, "committed", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TRAFFIC-SHAPER-REF":
                setattr(obj, "traffic_shaper_ref", ARRef.deserialize(child))

        return obj



class CouplingPortAsynchronousTrafficShaperBuilder(IdentifiableBuilder):
    """Builder for CouplingPortAsynchronousTrafficShaper with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CouplingPortAsynchronousTrafficShaper = CouplingPortAsynchronousTrafficShaper()


    def with_committed_burst(self, value: Optional[PositiveInteger]) -> "CouplingPortAsynchronousTrafficShaperBuilder":
        """Set committed_burst attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'committed_burst' is required and cannot be None")
        self._obj.committed_burst = value
        return self

    def with_committed(self, value: Optional[PositiveInteger]) -> "CouplingPortAsynchronousTrafficShaperBuilder":
        """Set committed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'committed' is required and cannot be None")
        self._obj.committed = value
        return self

    def with_traffic_shaper(self, value: Optional[SwitchAsynchronousTrafficShaperGroupEntry]) -> "CouplingPortAsynchronousTrafficShaperBuilder":
        """Set traffic_shaper attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'traffic_shaper' is required and cannot be None")
        self._obj.traffic_shaper = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "committed",
        "committedBurst",
        "trafficShaper",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CouplingPortAsynchronousTrafficShaper:
        """Build and return the CouplingPortAsynchronousTrafficShaper instance with validation."""
        self._validate_instance()
        return self._obj