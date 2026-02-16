"""IoHwAbstractionServerAnnotation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class IoHwAbstractionServerAnnotation(GeneralAnnotation):
    """AUTOSAR IoHwAbstractionServerAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("age", None, False, False, MultidimensionalTime),  # age
        ("argument", None, False, False, ArgumentDataPrototype),  # argument
        ("bsw_resolution", None, True, False, None),  # bswResolution
        ("data_element", None, False, False, VariableDataPrototype),  # dataElement
        ("failure", None, False, False, PortPrototype),  # failure
        ("filtering", None, False, False, FilterDebouncingEnum),  # filtering
        ("pulse_test", None, False, False, PulseTestEnum),  # pulseTest
        ("trigger", None, False, False, Trigger),  # trigger
    ]

    def __init__(self) -> None:
        """Initialize IoHwAbstractionServerAnnotation."""
        super().__init__()
        self.age: Optional[MultidimensionalTime] = None
        self.argument: Optional[ArgumentDataPrototype] = None
        self.bsw_resolution: Optional[Float] = None
        self.data_element: Optional[VariableDataPrototype] = None
        self.failure: Optional[PortPrototype] = None
        self.filtering: Optional[FilterDebouncingEnum] = None
        self.pulse_test: Optional[PulseTestEnum] = None
        self.trigger: Optional[Trigger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IoHwAbstractionServerAnnotation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IoHwAbstractionServerAnnotation":
        """Create IoHwAbstractionServerAnnotation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IoHwAbstractionServerAnnotation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IoHwAbstractionServerAnnotation since parent returns ARObject
        return cast("IoHwAbstractionServerAnnotation", obj)


class IoHwAbstractionServerAnnotationBuilder:
    """Builder for IoHwAbstractionServerAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IoHwAbstractionServerAnnotation = IoHwAbstractionServerAnnotation()

    def build(self) -> IoHwAbstractionServerAnnotation:
        """Build and return IoHwAbstractionServerAnnotation object.

        Returns:
            IoHwAbstractionServerAnnotation instance
        """
        # TODO: Add validation
        return self._obj
