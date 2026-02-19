"""DiagnosticControlDTCSetting AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 110)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ControlDTCSetting.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticControlDTCSetting(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticControlDTCSetting."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dtc_setting_class: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticControlDTCSetting."""
        super().__init__()
        self.dtc_setting_class: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticControlDTCSetting to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticControlDTCSetting, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dtc_setting_class
        if self.dtc_setting_class is not None:
            serialized = ARObject._serialize_item(self.dtc_setting_class, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DTC-SETTING-CLASS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticControlDTCSetting":
        """Deserialize XML element to DiagnosticControlDTCSetting object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticControlDTCSetting object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticControlDTCSetting, cls).deserialize(element)

        # Parse dtc_setting_class
        child = ARObject._find_child_element(element, "DTC-SETTING-CLASS")
        if child is not None:
            dtc_setting_class_value = child.text
            obj.dtc_setting_class = dtc_setting_class_value

        return obj



class DiagnosticControlDTCSettingBuilder:
    """Builder for DiagnosticControlDTCSetting."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlDTCSetting = DiagnosticControlDTCSetting()

    def build(self) -> DiagnosticControlDTCSetting:
        """Build and return DiagnosticControlDTCSetting object.

        Returns:
            DiagnosticControlDTCSetting instance
        """
        # TODO: Add validation
        return self._obj
