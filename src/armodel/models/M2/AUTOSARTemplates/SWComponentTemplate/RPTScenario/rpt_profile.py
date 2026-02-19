"""RptProfile AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 853)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptEnablerImplTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    PositiveInteger,
)


class RptProfile(Identifiable):
    """AUTOSAR RptProfile."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_service: Optional[PositiveInteger]
    min_service_point: Optional[PositiveInteger]
    service_point: Optional[CIdentifier]
    stim_enabler: Optional[RptEnablerImplTypeEnum]
    def __init__(self) -> None:
        """Initialize RptProfile."""
        super().__init__()
        self.max_service: Optional[PositiveInteger] = None
        self.min_service_point: Optional[PositiveInteger] = None
        self.service_point: Optional[CIdentifier] = None
        self.stim_enabler: Optional[RptEnablerImplTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize RptProfile to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptProfile, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_service
        if self.max_service is not None:
            serialized = ARObject._serialize_item(self.max_service, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_service_point
        if self.min_service_point is not None:
            serialized = ARObject._serialize_item(self.min_service_point, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-SERVICE-POINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_point
        if self.service_point is not None:
            serialized = ARObject._serialize_item(self.service_point, "CIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-POINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize stim_enabler
        if self.stim_enabler is not None:
            serialized = ARObject._serialize_item(self.stim_enabler, "RptEnablerImplTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STIM-ENABLER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptProfile":
        """Deserialize XML element to RptProfile object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptProfile object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptProfile, cls).deserialize(element)

        # Parse max_service
        child = ARObject._find_child_element(element, "MAX-SERVICE")
        if child is not None:
            max_service_value = child.text
            obj.max_service = max_service_value

        # Parse min_service_point
        child = ARObject._find_child_element(element, "MIN-SERVICE-POINT")
        if child is not None:
            min_service_point_value = child.text
            obj.min_service_point = min_service_point_value

        # Parse service_point
        child = ARObject._find_child_element(element, "SERVICE-POINT")
        if child is not None:
            service_point_value = ARObject._deserialize_by_tag(child, "CIdentifier")
            obj.service_point = service_point_value

        # Parse stim_enabler
        child = ARObject._find_child_element(element, "STIM-ENABLER")
        if child is not None:
            stim_enabler_value = RptEnablerImplTypeEnum.deserialize(child)
            obj.stim_enabler = stim_enabler_value

        return obj



class RptProfileBuilder:
    """Builder for RptProfile."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptProfile = RptProfile()

    def build(self) -> RptProfile:
        """Build and return RptProfile object.

        Returns:
            RptProfile instance
        """
        # TODO: Add validation
        return self._obj
