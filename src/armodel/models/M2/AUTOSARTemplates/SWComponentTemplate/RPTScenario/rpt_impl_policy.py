"""RptImplPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 202)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 854)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptEnablerImplTypeEnum,
    RptPreparationEnum,
)


class RptImplPolicy(ARObject):
    """AUTOSAR RptImplPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rpt_enabler_impl: Optional[RptEnablerImplTypeEnum]
    rpt_preparation_enum: Optional[RptPreparationEnum]
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
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize rpt_enabler_impl
        if self.rpt_enabler_impl is not None:
            serialized = ARObject._serialize_item(self.rpt_enabler_impl, "RptEnablerImplTypeEnum")
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
            serialized = ARObject._serialize_item(self.rpt_preparation_enum, "RptPreparationEnum")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse rpt_enabler_impl
        child = ARObject._find_child_element(element, "RPT-ENABLER-IMPL")
        if child is not None:
            rpt_enabler_impl_value = RptEnablerImplTypeEnum.deserialize(child)
            obj.rpt_enabler_impl = rpt_enabler_impl_value

        # Parse rpt_preparation_enum
        child = ARObject._find_child_element(element, "RPT-PREPARATION-ENUM")
        if child is not None:
            rpt_preparation_enum_value = RptPreparationEnum.deserialize(child)
            obj.rpt_preparation_enum = rpt_preparation_enum_value

        return obj



class RptImplPolicyBuilder:
    """Builder for RptImplPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptImplPolicy = RptImplPolicy()

    def build(self) -> RptImplPolicy:
        """Build and return RptImplPolicy object.

        Returns:
            RptImplPolicy instance
        """
        # TODO: Add validation
        return self._obj
