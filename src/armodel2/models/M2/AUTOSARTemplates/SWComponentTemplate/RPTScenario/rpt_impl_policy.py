"""RptImplPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 202)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 854)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptEnablerImplTypeEnum,
    RptPreparationEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RptImplPolicy(ARObject):
    """AUTOSAR RptImplPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RPT-IMPL-POLICY"


    rpt_enabler_impl: Optional[RptEnablerImplTypeEnum]
    rpt_preparation_enum: Optional[RptPreparationEnum]
    _DESERIALIZE_DISPATCH = {
        "RPT-ENABLER-IMPL": lambda obj, elem: setattr(obj, "rpt_enabler_impl", RptEnablerImplTypeEnum.deserialize(elem)),
        "RPT-PREPARATION-ENUM": lambda obj, elem: setattr(obj, "rpt_preparation_enum", RptPreparationEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize RptImplPolicy."""
        super().__init__()
        self.rpt_enabler_impl: Optional[RptEnablerImplTypeEnum] = None
        self.rpt_preparation_enum: Optional[RptPreparationEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize RptImplPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptImplPolicy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rpt_enabler_impl
        if self.rpt_enabler_impl is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_enabler_impl, "RptEnablerImplTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-ENABLER-IMPL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_preparation_enum
        if self.rpt_preparation_enum is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_preparation_enum, "RptPreparationEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-PREPARATION-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptImplPolicy":
        """Deserialize XML element to RptImplPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptImplPolicy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptImplPolicy, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RPT-ENABLER-IMPL":
                setattr(obj, "rpt_enabler_impl", RptEnablerImplTypeEnum.deserialize(child))
            elif tag == "RPT-PREPARATION-ENUM":
                setattr(obj, "rpt_preparation_enum", RptPreparationEnum.deserialize(child))

        return obj



class RptImplPolicyBuilder(BuilderBase):
    """Builder for RptImplPolicy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptImplPolicy = RptImplPolicy()


    def with_rpt_enabler_impl(self, value: Optional[RptEnablerImplTypeEnum]) -> "RptImplPolicyBuilder":
        """Set rpt_enabler_impl attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rpt_enabler_impl' is required and cannot be None")
        self._obj.rpt_enabler_impl = value
        return self

    def with_rpt_preparation_enum(self, value: Optional[RptPreparationEnum]) -> "RptImplPolicyBuilder":
        """Set rpt_preparation_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rpt_preparation_enum' is required and cannot be None")
        self._obj.rpt_preparation_enum = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "rptEnablerImpl",
        "rptPreparationEnum",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RptImplPolicy:
        """Build and return the RptImplPolicy instance with validation."""
        self._validate_instance()
        return self._obj