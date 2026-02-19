"""ISignalTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 330)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 229)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_group import (
    ISignalGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_port import (
    ISignalPort,
)


class ISignalTriggering(Identifiable):
    """AUTOSAR ISignalTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_signal: Optional[ISignal]
    i_signal_group_ref: Optional[ARRef]
    i_signal_ports: list[ISignalPort]
    def __init__(self) -> None:
        """Initialize ISignalTriggering."""
        super().__init__()
        self.i_signal: Optional[ISignal] = None
        self.i_signal_group_ref: Optional[ARRef] = None
        self.i_signal_ports: list[ISignalPort] = []
    def serialize(self) -> ET.Element:
        """Serialize ISignalTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignalTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_signal
        if self.i_signal is not None:
            serialized = ARObject._serialize_item(self.i_signal, "ISignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_group_ref
        if self.i_signal_group_ref is not None:
            serialized = ARObject._serialize_item(self.i_signal_group_ref, "ISignalGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-SIGNAL-GROUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_signal_ports (list to container "I-SIGNAL-PORTS")
        if self.i_signal_ports:
            wrapper = ET.Element("I-SIGNAL-PORTS")
            for item in self.i_signal_ports:
                serialized = ARObject._serialize_item(item, "ISignalPort")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalTriggering":
        """Deserialize XML element to ISignalTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalTriggering, cls).deserialize(element)

        # Parse i_signal
        child = ARObject._find_child_element(element, "I-SIGNAL")
        if child is not None:
            i_signal_value = ARObject._deserialize_by_tag(child, "ISignal")
            obj.i_signal = i_signal_value

        # Parse i_signal_group_ref
        child = ARObject._find_child_element(element, "I-SIGNAL-GROUP")
        if child is not None:
            i_signal_group_ref_value = ARObject._deserialize_by_tag(child, "ISignalGroup")
            obj.i_signal_group_ref = i_signal_group_ref_value

        # Parse i_signal_ports (list from container "I-SIGNAL-PORTS")
        obj.i_signal_ports = []
        container = ARObject._find_child_element(element, "I-SIGNAL-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_signal_ports.append(child_value)

        return obj



class ISignalTriggeringBuilder:
    """Builder for ISignalTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalTriggering = ISignalTriggering()

    def build(self) -> ISignalTriggering:
        """Build and return ISignalTriggering object.

        Returns:
            ISignalTriggering instance
        """
        # TODO: Add validation
        return self._obj
