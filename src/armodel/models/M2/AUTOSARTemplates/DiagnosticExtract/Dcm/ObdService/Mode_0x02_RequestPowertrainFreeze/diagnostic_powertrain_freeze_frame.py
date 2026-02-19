"""DiagnosticPowertrainFreezeFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 153)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x02_RequestPowertrainFreeze.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticPowertrainFreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticPowertrainFreezeFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    pids: list[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticPowertrainFreezeFrame."""
        super().__init__()
        self.pids: list[DiagnosticParameter] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticPowertrainFreezeFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticPowertrainFreezeFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize pids (list to container "PIDS")
        if self.pids:
            wrapper = ET.Element("PIDS")
            for item in self.pids:
                serialized = ARObject._serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticPowertrainFreezeFrame":
        """Deserialize XML element to DiagnosticPowertrainFreezeFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticPowertrainFreezeFrame object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticPowertrainFreezeFrame, cls).deserialize(element)

        # Parse pids (list from container "PIDS")
        obj.pids = []
        container = ARObject._find_child_element(element, "PIDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pids.append(child_value)

        return obj



class DiagnosticPowertrainFreezeFrameBuilder:
    """Builder for DiagnosticPowertrainFreezeFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticPowertrainFreezeFrame = DiagnosticPowertrainFreezeFrame()

    def build(self) -> DiagnosticPowertrainFreezeFrame:
        """Build and return DiagnosticPowertrainFreezeFrame object.

        Returns:
            DiagnosticPowertrainFreezeFrame instance
        """
        # TODO: Add validation
        return self._obj
