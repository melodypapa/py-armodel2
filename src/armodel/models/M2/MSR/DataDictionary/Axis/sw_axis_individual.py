"""SwAxisIndividual AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
    ApplicationPrimitiveDataType,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr import (
    DataConstr,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_generic import (
    SwAxisGeneric,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
    SwVariableRefProxy,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class SwAxisIndividual(SwCalprmAxisTypeProps):
    """AUTOSAR SwAxisIndividual."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compu_method", None, False, False, CompuMethod),  # compuMethod
        ("data_constr", None, False, False, DataConstr),  # dataConstr
        ("input_variable", None, False, False, ApplicationPrimitiveDataType),  # inputVariable
        ("sw_axis_generic", None, False, False, SwAxisGeneric),  # swAxisGeneric
        ("sw_max_axis", None, True, False, None),  # swMaxAxis
        ("sw_min_axis", None, True, False, None),  # swMinAxis
        ("sw_variable_ref_proxies", None, False, True, SwVariableRefProxy),  # swVariableRefProxies
        ("unit", None, False, False, Unit),  # unit
    ]

    def __init__(self) -> None:
        """Initialize SwAxisIndividual."""
        super().__init__()
        self.compu_method: Optional[CompuMethod] = None
        self.data_constr: Optional[DataConstr] = None
        self.input_variable: Optional[ApplicationPrimitiveDataType] = None
        self.sw_axis_generic: Optional[SwAxisGeneric] = None
        self.sw_max_axis: Optional[Integer] = None
        self.sw_min_axis: Optional[Integer] = None
        self.sw_variable_ref_proxies: list[SwVariableRefProxy] = []
        self.unit: Optional[Unit] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwAxisIndividual to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisIndividual":
        """Create SwAxisIndividual from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwAxisIndividual instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwAxisIndividual since parent returns ARObject
        return cast("SwAxisIndividual", obj)


class SwAxisIndividualBuilder:
    """Builder for SwAxisIndividual."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisIndividual = SwAxisIndividual()

    def build(self) -> SwAxisIndividual:
        """Build and return SwAxisIndividual object.

        Returns:
            SwAxisIndividual instance
        """
        # TODO: Add validation
        return self._obj
