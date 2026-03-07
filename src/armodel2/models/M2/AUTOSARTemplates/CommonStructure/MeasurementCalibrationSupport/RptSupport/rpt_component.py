"""RptComponent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
    RoleBasedMcDataAssignment,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_executable_entity import (
    RptExecutableEntity,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_impl_policy import (
    RptImplPolicy,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RptComponent(Identifiable):
    """AUTOSAR RptComponent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RPT-COMPONENT"


    mc_datas: list[RoleBasedMcDataAssignment]
    rp_impl_policy: Optional[RptImplPolicy]
    rpt_executable_entities: list[RptExecutableEntity]
    _DESERIALIZE_DISPATCH = {
        "MC-DATAS": lambda obj, elem: obj.mc_datas.append(SerializationHelper.deserialize_by_tag(elem, "RoleBasedMcDataAssignment")),
        "RP-IMPL-POLICY": lambda obj, elem: setattr(obj, "rp_impl_policy", SerializationHelper.deserialize_by_tag(elem, "RptImplPolicy")),
        "RPT-EXECUTABLE-ENTITYS": lambda obj, elem: obj.rpt_executable_entities.append(SerializationHelper.deserialize_by_tag(elem, "RptExecutableEntity")),
    }


    def __init__(self) -> None:
        """Initialize RptComponent."""
        super().__init__()
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.rp_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_executable_entities: list[RptExecutableEntity] = []

    def serialize(self) -> ET.Element:
        """Serialize RptComponent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptComponent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mc_datas (list to container "MC-DATAS")
        if self.mc_datas:
            wrapper = ET.Element("MC-DATAS")
            for item in self.mc_datas:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedMcDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rp_impl_policy
        if self.rp_impl_policy is not None:
            serialized = SerializationHelper.serialize_item(self.rp_impl_policy, "RptImplPolicy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RP-IMPL-POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_executable_entities (list to container "RPT-EXECUTABLE-ENTITYS")
        if self.rpt_executable_entities:
            wrapper = ET.Element("RPT-EXECUTABLE-ENTITYS")
            for item in self.rpt_executable_entities:
                serialized = SerializationHelper.serialize_item(item, "RptExecutableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptComponent":
        """Deserialize XML element to RptComponent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptComponent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptComponent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MC-DATAS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mc_datas.append(SerializationHelper.deserialize_by_tag(item_elem, "RoleBasedMcDataAssignment"))
            elif tag == "RP-IMPL-POLICY":
                setattr(obj, "rp_impl_policy", SerializationHelper.deserialize_by_tag(child, "RptImplPolicy"))
            elif tag == "RPT-EXECUTABLE-ENTITYS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.rpt_executable_entities.append(SerializationHelper.deserialize_by_tag(item_elem, "RptExecutableEntity"))

        return obj



class RptComponentBuilder(IdentifiableBuilder):
    """Builder for RptComponent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptComponent = RptComponent()


    def with_mc_datas(self, items: list[RoleBasedMcDataAssignment]) -> "RptComponentBuilder":
        """Set mc_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_datas = list(items) if items else []
        return self

    def with_rp_impl_policy(self, value: Optional[RptImplPolicy]) -> "RptComponentBuilder":
        """Set rp_impl_policy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rp_impl_policy' is required and cannot be None")
        self._obj.rp_impl_policy = value
        return self

    def with_rpt_executable_entities(self, items: list[RptExecutableEntity]) -> "RptComponentBuilder":
        """Set rpt_executable_entities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_executable_entities = list(items) if items else []
        return self


    def add_mc_data(self, item: RoleBasedMcDataAssignment) -> "RptComponentBuilder":
        """Add a single item to mc_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_datas.append(item)
        return self

    def clear_mc_datas(self) -> "RptComponentBuilder":
        """Clear all items from mc_datas list.

        Returns:
            self for method chaining
        """
        self._obj.mc_datas = []
        return self

    def add_rpt_executable_entity(self, item: RptExecutableEntity) -> "RptComponentBuilder":
        """Add a single item to rpt_executable_entities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_executable_entities.append(item)
        return self

    def clear_rpt_executable_entities(self) -> "RptComponentBuilder":
        """Clear all items from rpt_executable_entities list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_executable_entities = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "mcData",
        "rpImplPolicy",
        "rptExecutableEntity",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RptComponent:
        """Build and return the RptComponent instance with validation."""
        self._validate_instance()
        return self._obj